# Connecting to a PostgreSQL database

In this task we will create a container with a PostgreSQL database and one that runs some SQL scripts against it.

## PostgreSQL database

We can use the official [PostgreSQL](https://hub.docker.com/_/postgres) Docker image to run our database.

- **Start a container using the `docker run` command:**

```
docker run --name my-postgres -e POSTGRES_PASSWORD=mysecretpassword -d postgres
```

## Running some SQL queries against the database

We will run some SQL queries against the database using our `db.py` script.

This script will create a table if it does not already exist, insert some values to the database, then print the resulting values.

Your `db-script` image should:
1) Extend the `python:3.6` image.
2) Install the `psycopg2` python library using the command `pip3 install psycopg2`.
3) Copy and run the `db.py` script.

**Build image**
```
docker build --tag db-script .
```

**Run container**
```
docker run --rm db-script
```

You should see a connection error in the output. This is because our container can't reach the database.

**Why not?**

We did not have the same issue in the previous task when we had a website and an API running in separate containers.

**Why not?**

Let's try accessing it using a Docker `link` or `network` instead.

## Using link
Try accessing it through a [docker link](https://docs.docker.com/network/links/) using the `--link` flag when running the `db-script` container.

The flag can be used like this:
```
--link <name or id>:alias
```

Here `name` is the name of the container we’re linking to (`my-postgres` in our case) and  `alias` is an alias for the link name. We can connect to the linked container by using the alias as host name.

Our script looks for a value from the `DB_HOST` environment variable. We can override this value by using the `-e` flag when running the container like this:
```
docker run -e "<environment_variable>=<value> ..."
```

- **Run the following command:**

```
docker run --rm --link my-postgres:postgres-host -it -e "DB_HOST=postgres-host" db-script
```

You should now see some values printed in the output from running the container.

## Using network
Container links are a legacy feature that might be removed, so Docker suggest we should use a [network](https://docs.docker.com/network/) instead.

We will create a `bridge` network that our containers can use to communicate.

- **Create a network for this application using the `docker network` command:**

```
docker network create postgres-network
```

You can inspect this network with the command:
```
docker network inspect postgres-network
```

It should contain something like this:
```
[
    {
        "Name": "postgres-network",
        "Id": "ac36598a15db59882da1644db24a07147572fdce065de779ed83693487d3206b",
        "Created": "2020-01-26T20:36:25.480091569+01:00",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": {},
            "Config": [
                {
                    "Subnet": "172.18.0.0/16",
                    "Gateway": "172.18.0.1"
                }
            ]
        },
        "Internal": false,
        "Attachable": false,
        "Ingress": false,
        "ConfigFrom": {
            "Network": ""
        },
        "ConfigOnly": false,
        "Containers": {},
        "Options": {},
        "Labels": {}
    }
]
```

- **Start your containers in this network:**

```
docker run --name my-postgres --net postgres-network  -e POSTGRES_PASSWORD=mysecretpassword -d postgres
```

NOTE: You may have to stop and remove the previous `my-postgres` container first:
```
docker stop my-postgres
docker rm my-postgres
```

Once you have started the `my-postgres` container you can inspect the network with the following command:
```
docker network inspect postgres-network
```

The output should look something like this:
```
[
    {
        "Name": "postgres-network",
        "Id": "bbf4ce8bc45f3adee2ce7960c0de18289b870ac4bf9c00c79269a288c257ac6a",
        "Created": "2020-01-27T10:48:04.72173886+01:00",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": {},
            "Config": [
                {
                    "Subnet": "172.18.0.0/16",
                    "Gateway": "172.18.0.1"
                }
            ]
        },
        "Internal": false,
        "Attachable": false,
        "Ingress": false,
        "ConfigFrom": {
            "Network": ""
        },
        "ConfigOnly": false,
        "Containers": {
            "c53be40f7aba9b266b57850659eb47439d373b68db54110b6a657c5873a8eb56": {
                "Name": "my-postgres",
                "EndpointID": "6ae98da080e60b6d173ed1d21931a26ff415f391453aaeabe35c04335ea1beeb",
                "MacAddress": "02:42:ac:12:00:02",
                "IPv4Address": "172.18.0.2/16",
                "IPv6Address": ""
            }
        },
        "Options": {},
        "Labels": {}
    }
]
```

You can see that it includes the `my-postgres` container which has the IPv4Address `172.18.0.2`

Let's use this value as `DB_HOST` when running our `db-script` container.

```
docker run --rm --net postgres-network -e "DB_HOST=<my-postgres:IPv4Address>" db-script
```

Make sure to replace `<my-postgres:IPv4Address>` with the actual value.

In our case the value of `my-postgres:IPv4Address` is `172.18.0.2` (collected from the `docker network inspect postgres-network` output above), but you might get a different value.

- **Try running the `db-script` container a couple of times.**

Does the output change for each run? Why/why not?

- **Try terminating the `my-postgres` container and create a new one, then run the `db-script` container again**

Did the output change from last time? Why/why not?
