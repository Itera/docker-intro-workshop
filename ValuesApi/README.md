# Values API
Simple API used to fetch static values. You can also store and get values from a redis cache.

## Requirements
In order to build and run this API you need to install [.NET Core 2.2](https://dotnet.microsoft.com/download/dotnet-core/2.2)

Alternatively you can build it with docker using the [.NET Core images](https://hub.docker.com/_/microsoft-dotnet-core)

## How to build
This command will build the API and store the result in the `out` folder:
```
dotnet publish ValuesApi.csproj -c Release -o out
```

## How to run
After building the API you can run it using the following command:
```
dotnet out/ValuesApi.dll
```

## Configuration
You can configure the redis endpoint by setting the `RedisEndpoint` environment variable. The default value is `http://localhost:6379`

## Swagger
An interactive API documentation is available at the /swagger endpoint after launching the API.
