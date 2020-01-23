# Hosting a static website

The goal of this task is to serve a website on localhost:8080

We will do this with docker using the [nginx image](https://hub.docker.com/_/nginx).

- **Clone the repository and navigate to this folder**

## Using mounted volume
We will first solve this by running the base nginx image and mounting the current directory into the /usr/share/nginx/html folder in the container.

- **Run the following command:**

```
docker run --rm --name my-static-website --publish 8080:80 --volume $(pwd):/usr/share/nginx/html:ro nginx
```

NOTE: If you are using Windows you can run it in Powershell by replacing `$(pwd)` with `${pwd}`.

You should then be able to view the website by opening http://localhost:8080 in a browser.

- **Try changing the content of the index.html file and reload the webpage**

Did the content change? Why/why not?

## Using custom image
In this task we will copy the index.html file into the container instead of mounting our local file system.

- **Modify the Dockerfile so that it inherits from the nginx image and adds a copy of the `index.html` file to the `/usr/share/nginx/html` folder in the container.**

Checkout the [Dockerfile reference](https://docs.docker.com/engine/reference/builder/) if you need any more guidance.


- **Create an image from your Dockerfile using the `docker build` command:**
```
docker build --tag static-website .
```

- **Start a container from the image using the `docker run` command:**
```
docker run --rm --publish 8080:80 static-website
```

You should then be able to view the website by opening http://localhost:8080 in a browser.

- **Try changing the content of the index.html file and reload the webpage.**

Did the content change? Why/why not?
