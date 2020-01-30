# Hosting a static website

The goal of this task is to serve a website on [http://localhost:8080](http:localhost:8080). This is just a fancy way of saying that we will download a webpage when we open that link in our browser. The webpage in question is the `index.html` file in this folder.

We will serve the website using a webserver called [NGINX](https://www.nginx.com/products/nginx/).

Since we don't want to install and configure nginx ourselves, we will create a Docker image that extends the official [nginx image](https://hub.docker.com/_/nginx).

## Run the image

The nginx image will listen to requests on port 80, so we need to expose port 80 on the container on port 8080 on our system.

- **Start a container from the nginx image with the `docker run` command:**
```
docker run --rm --publish 8080:80 nginx
```

You should see a nginx welcome message if you open http://localhost:8080

## Using mounted volume
We want to see our own website instead of the welcome message. We will first solve this by mounting the current directory (this folder) into the `/usr/share/nginx/html` folder in the `nginx` container. We can do this by adding the `--volume` flag to the command.

- **Run the following command:**
```
docker run --rm --publish 8080:80 --volume $(pwd):/usr/share/nginx/html:ro nginx
```

NOTE: If you are using Windows you can run it in Powershell by replacing `$(pwd)` with `${pwd}`.

You should then be able to view the website by opening http://localhost:8080 in a browser.

- **Try changing the content of the index.html file and reload the webpage**

Did the content change? Why/why not?

## Using custom image
In this task we will copy the index.html file into the container instead of mounting our local file system.

- **Write a Dockerfile that:**
1) Extends from the `nginx` image
2) Copies the `index.html` file to the `/usr/share/nginx/html` folder in the image

The relevant Dockerfile commands are `FROM <base_image_name>` and `COPY <from (our filesystem)> <to (container filesystem)>`.

See the [Dockerfile reference](https://docs.docker.com/engine/reference/builder/) for reference.


- **Create an image from your Dockerfile using the `docker build` command:**
```
docker build --tag my-static-website .
```

- **Start a container from the image using the `docker run` command:**
```
docker run --rm --publish 8080:80 my-static-website
```

You should then be able to view the website by opening http://localhost:8080 in a browser.

- **Try changing the content of the index.html file and reload the webpage.**

Did the content change? Why/why not?