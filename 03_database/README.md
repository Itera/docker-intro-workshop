# Connecting to a PostgreSQL database

In this task we will create a container with a PostgreSQL database and a container that runs some SQL scripts against it.

## PostgreSQL database

We can use the official [PostgreSQL](https://hub.docker.com/_/postgres) Docker image to run our database.

- **Start a container using the `docker run` command:**

```
docker run --name my-postgres -e POSTGRES_PASSWORD=mysecretpassword -d postgres
```

:information_source: The `--env` or `-e` flag let us specify environment variables in the container.

:information_source: The `--detach` or `-d` flag let us run a container in the background without locking our terminal.

:information_source: The `--name` tag gives our container a known name so that we can easily stop or remove it later by referring to its name.

Since we gave our container a name we are now able to:
- Stop the container: `docker stop my-postgres`
- Start the container: `docker start my-postgres`
- Remove the container: `docker rm my-postgres`

If we didn't give it a name we would have to find the auto-generated name using the `docker ps` command.

## Running some SQL queries against the database

We will run some SQL queries against the database using our `db.py` script.

This script will create a table if it does not already exist, insert some values to the database, then print the resulting values.

Your `db-script` image should:
1) Extend the `python:3.6` image.
2) Install the `psycopg2` python library using the command `pip3 install psycopg2`.
3) Copy the `db.py` script.
4) Run the `db.py` script using the command `python3 db.py`.

- **Build image**
```
docker build --tag db-script .
```

- **Run container**
```
docker run --rm db-script
```

You should see a connection error in the output. This is because our container can't reach the database.

:question: Question 3.1: Why not?

We did not have the same issue in the previous task when we had a website and an API running in separate containers.

:question: Question 3.2: Why not?

Let's try accessing it using a Docker `network` instead.

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

You can see that it includes the `my-postgres` container which has the IPv4Address `172.18.0.2`. This might be a different value in your network.

### Using explicit IP address as host name
One way to connect to the `my-postgres` container from our `db-script` container is to use this IP address as host name:
```
docker run --rm --net postgres-network -e "DB_HOST=172.18.0.2" db-script
```

Make sure to use the actual IP address from your previous output.

### Using container name as host name
Containers on user-defined bridge networks can resolve each other by name or alias, so a better solution is to use the container name as host name, like we did with the link:

```
docker run --rm --net postgres-network -e "DB_HOST=my-postgres" db-script
```

This way we don't have to find the correct IP address first.

- **Try running the `db-script` container a couple of times.**

:question: Question 3.3: Does the output change for each run? Why/why not?

- **Try to stop and remove the `my-postgres` container and create a new one, then run the `db-script` container again**

:question: Question 3.4: Did the output change from last time? Why/why not?

## Persist our data in a volume

We can create and mount a Docker volume in order to persist the state between each time we create a new postgresql container.

### Create a volume

In order to do this we first need to create a volume:

```
docker volume create postgresql-volume
```

You can inspect the volume to see where on your machine the data is stored:
```
docker volume inspect postgresql-volume
```

The data is stored in the `Mountpoint` path on your machine.

### Mount the volume to our `my-postgresql` container

Next we need to mount the volume to our container. Our container stores its data in the `/var/lib/postgresql/data` directory by default.

We can mount the volume by using the `--mount` flag:
```
docker run --name my-postgres -e POSTGRES_PASSWORD=mysecretpassword -d --mount type=volume,source=<name_of_our_volume>,destination=<directory_on_the_container> postgres
```

### Verify that our data is persisted

- **Try running the db-script container again**

:information_source: Remember that you need to either use a link or network to reach the container.

- **Look at the files in the `Mountpoint` path on your machine**

:question: Are there any new files there?

- **Try to stop and remove the `my-postgres` container and create a new one (with the same mounted volume), then run the `db-script` container again**

:question: Question 3.5: Did we still have the values from our previous run? Why/why not?
