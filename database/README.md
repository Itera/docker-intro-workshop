# Connecting to a PostgreSQL database

In this task we will create a container with a PostgreSQL database and one that runs some SQL scripts against it.

## PostgreSQL database

We can use the official [PostgreSQL](https://hub.docker.com/_/postgres) Docker image to run our database.

- ** Start a container using the `docker run` command:**

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

Run container:
```
docker run --rm db-script
```

You should see a connection error in the output. This is because our container can't reach the database.

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

You should noe see some values printed in the output from running the container.

## Using network
Container links are a legacy feature that might be removed, so Docker suggest we should use a [network](https://docs.docker.com/network/) instead.

We will create a `bridge` network that our containers can use to communicate.

- **Create a network for this application using the `docker network` command:**

```
docker network create postgres-network
```

- **Start your containers in this network:**

```
docker run --name my-postgres --net postgres-network  -e POSTGRES_PASSWORD=mysecretpassword -d postgres
```

```
docker run --rm --net postgres-network -it db-script
```

- **Try running the `db-script` container a couple of times.**

**Does the output change for each run? Why/why not?**

- **Try terminating the `my-postgres` container and create a new one, then run the `db-script` container again**

**Did the output change from last time? Why/why not?**
