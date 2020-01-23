# API with redis integration

The goal of this task is to read and write values to a [redis cache](https://redis.io/) by using an API.

The API and the redis cache should run in separate containers.

## API
The code for the API we will use is in the [ValuesApi](../ValuesApi) folder.

This is the same API used in the dynamic website task so you should be able to reuse your image from that task.

## Redis
We will use the [redis image](https://hub.docker.com/_/redis) for our redis cache.

- **Start a container using the `docker run` command:**

```
docker run --rm --name values-redis --publish 6379:6379 redis
```

## Accessing redis via the API
We can now access our redis cache on `localhost:6379`, but our API can't reach it. **Why not?**

Let's try to access it using a docker network or link instead.

## Using link
Try accessing it through a [docker link](https://docs.docker.com/network/links/) using the `--link` flag when running the values-api container.

The flag can be used like this:
```
--link <name or id>:alias
```

Where `name` is the name of the container we’re linking to and  `alias` is an alias for the link name. We can connect to the linked container by using the alias as host name.

In order to connect to the alias instead of `http://localhost:6379` we need to update the `RedisEndpoint` configuration in our API.

One way to do this is by updating the value in [appsettings.json](../ValuesApi/appsettings.json), but this would require us to build a new container each time we update the alias name.

Our API is configured to look for config values from environment variables as well, so we can override the endpoint by setting the `RedisEndpoint` environment variable when we run the container like this:
```
docker run -e "<environment_variable>=<value> ..."
```

- **Run the following command:**

```
docker run --rm --link values-redis:redis-endpoint --publish 5000:80 -it -e "RedisEndpoint=redis-endpoint" values-api
```

## Using network

Container links are a legacy feature that might be removed, so Docker suggest we should use a [network](https://docs.docker.com/network/) instead.

We will create a `bridge` network that our containers can use to communicate.

- **Create a network for this application using the `docker network` command:**

```
docker network create redis-api-net
```

- **Start your containers in this network:**

```
docker run --rm --name values-redis --net redis-api-net --publish 6379:6379 redis
```

```
docker run --rm --net redis-api-net --publish 5000:80 -it -e "RedisEndpoint=values-redis" values-api
```

The `/api/redis` endpoints are available in the swagger documentation for the API on http://localhost:5000/swagger

- **Try adding and reading values from the redis cache using the endpoints**

- **Try terminating the redis container and create a new one**

Does it still contain the values we stored previously? Why/why not?
