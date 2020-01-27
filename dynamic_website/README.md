# Fetching content from an API

The goal of this task is to serve a website on `localhost:8080` that fetches some content from an API at `localhost:5000/value` and renders the result.

## Website
We can serve the website the same way as we did for the [static website](../static_website), so you can reuse your Dockerfile from that task.

**Note that we have a new index.html file in this task so we need to build a new image that copies the correct file.**

**Write a `Dockerfile-website` that:**
1) Inherits from the `nginx` base image
2) Copies the index.html file to the `/usr/share/nginx/html` folder on the image

### Build new image for the website
```
docker build --tag dynamic-website -f Dockerfile-website .
```

### Run container
```
docker run --rm -p 8080:80 dynamic-website
```

## API
The code for the API we will use is in the `api.py` file.

This API should be run in a separate container.

It is written in python, so our image needs to have the correct version of python installed. We also need to install some 3rd party libraries.

We can extend the official [python](https://hub.docker.com/_/python) image to ensure that we have the correct version of python. In this case we will use `python:3.6`.

The 3rd party requirements we need are listed in the `requirements.txt` file. We can install these with the python package manager using the `pip3` command:

```
pip3 install -r requirements.txt
```

Finally we can run the api using the `python3` command:
```
python3 api.py
```

**Write a `Dockerfile-api` that:**
1) Inherits from the `python:3.6` base image
2) Copies the `requirements.txt` and `api.py` files to the image
3) Installs the requirements for the API
4) Runs the API

- **Create an image from your Dockerfile using the `docker build` command:**
```
docker build --tag flask-api -f Dockerfile-api .
```

The API will listen to port 5000 so we need to expose port 5000 on the container on port 5000 on our system.

- **Start a container from the image using the `docker run` command:**
```
docker run --rm --publish 5000:5000 flask-api
```

You can verify that you are able to reach the API by loading its documentation page at http://localhost:5000/apidocs/

You should now be able to view the website by opening http://localhost:8080 in a browser.

Can you see the value we got from the API? Try reloading the page and see if the value changes.
