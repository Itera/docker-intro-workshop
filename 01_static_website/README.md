# Hosting a static website :web:

The goal of this task is to serve a website on [http://localhost:8080](http:localhost:8080). This is just a fancy way of saying that we will download a webpage when we open that link in our browser. The webpage in question is the `index.html` file in this folder.

We will serve the website using a webserver called [NGINX](https://www.nginx.com/products/nginx/).

Since we don't want to install and configure nginx ourselves, we will create a Docker image that extends the official [nginx image](https://hub.docker.com/_/nginx).

## Run the image

The nginx image will listen to HTTP requests on port 80, so we need to expose port 80 on the container on port 8080 on our system.

- **Start a container from the nginx image with the `docker run` command:**
```
docker run --rm --publish 8080:80 nginx
```

:information_source: The `--rm` flag is added in order to automatically remove the container when it exits.

:information_source: The `--publish` or `-p` flag is added in order to map port 8080 on our system to port 80 on the container.

You should see a nginx welcome message if you open http://localhost:8080 in a browser.

## Using a bind mount
We want to see our own website instead of the welcome message. We can solve this by putting the `index.html` file into the `/usr/share/nginx/html` folder in the container.

We will first solve this by mounting the current directory (this folder) into the `/usr/share/nginx/html` folder in the `nginx` container.

We can do this by adding the `-v`/`--volume` flag or the `--mount` flag to the command.

### Using the --volume flag
The `--volume` flag taks an argument that is divided into 3 separated by `:`.

- The first part is the path to the file or directory on the host machine.
- The second part is the path where the file or directory is mounted in the container
- The third part is optional, and is a comma-separated list of options. In this case we use the `ro` (readonly) option, because we don't want the container to write changes to the file.

- **Run the following command:**
```
docker run --rm --publish 8080:80 --volume $(pwd):/usr/share/nginx/html:ro nginx
```

:information_source: If you are using Windows you can run it in Powershell by replacing `$(pwd)` with `${pwd}`.

:information_source: If you get the following error `docker: invalid reference format.`, try wrapping the volume fields with double quotes, i.e. `--volume "$(pwd):/usr/share/nginx/html:ro"`.

### Using the --mount flag
The `--mount` flag takes an argument with `<key>=<value>` pairs, separated by `,`.

It's a bit more verbose, but easier to understand.

```
docker run --rm --publish 8080:80 --mount type=bind,source=$(pwd),destination=/usr/share/nginx/html,readonly nginx
```

You should now be able to view the website by opening http://localhost:8080 in a browser.

- **Try changing the content of the index.html file and reload the webpage**

:question: Question 1.1: Did the content change? Why/why not?

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

:information_source: The `--tag` or `-t` flag is used to give our image a name.

Congratulations! :trophy: You have now built your first Docker image. You should be able to see your image if you run the `docker images` command. We are now ready to run a container using our freshly built image.

- **Start a container from the `my-static-website` image using the `docker run` command:**
```
docker run --rm --publish 8080:80 my-static-website
```

You should now be able to view the website by opening http://localhost:8080 in a browser.

- **Try changing the content of the index.html file and reload the webpage.**

:question: Question 1.2: Did the content change? Why/why not?
