# Bonus task

If you have completed all the other tasks you can attempt this one. It will require you to use all the skills you have aquired so far.

The goal is to build and run an API that will read and write values to a redis cache.

The API and redis server will run in separate containers so they need to communicate through a link or network.

The redis cahce should persist its data in a volume so that we don't lose the stored values when we create a new redis container.

## Redis
We can use the official `redis` image for our redis server.

### Creating a volume

First we need to create a volume using the `docker volume create <volume_name>` command.

### Mounting the volume

We can mount the volume when we start the redis server with the `--mount` flag:

```
--mount type=volume,source=<volume_name>,destination=<container_path>
```

The redis container stores data in the `/data` directory by default.

### Starting the redis server

We can start the redis server with persistent storage the command:
```
docker run --name <container_name> -d redis redis-server --appendonly yes
```

:information_source: Remember to mount your volume when you start the container.

:information_source: The redis server listens to requests on port 6379.

## API

The source code for our API is on the [ValuesApi](ValuesApi) folder. In order to build our API we need the .NET Core SDK. We can use the `mcr.microsoft.com/dotnet/core/sdk:2.2` image for this.

### Building the API

We can build the API with the `dotnet publish` command:

```
dotnet publish ValuesApi.csproj -c Release -o out
```

### Running the API

We can run the API with the dotnet command:

```
dotnet out/ValuesApi.dll
```

### Build API image
Create a Dockerfile that copies the source code, builds the API, then runs the API using the commands above then build an image:
```
docker build --tag <image_name> .
```

### Start API container

:information_source: The API listens to port 80, so we need to map the port we want to call the API from on our machine to port 80 in the container using the `--publish` flag.

:information_source: The API needs to be configured with the hostname for the redis server. This can be set via the `RedisEndpoint` environment variable.

:information_source: In order for the API to reach the redis server we need to access it using either a docker link or a network.

In this example we use port 5000 on our machine:
```
docker run -d --publish 5000:80 -e "RedisEndpoint=<redis_host>" <image_name>
```

## Testing our solution

Once everything is up and running you should be able to access the API's swagger documentation on http://localhost:5000/swagger

- **Try adding some values using the POST api/redis endpoint***

- **Verify that you can get the inserted values using the GET api/redis endpoint**

- **Stop and remove the redis container and create a new one**

- **Verify that you get your old values when you call the GET api/redis endpoint**
