# Fetching content from an API

The goal of this task is to serve a website on `localhost:8080` that fetches some content from an API at `localhost:5000/value` and renders the result.

## Website
We can serve the website the same way as we did for the [static website](../static_website), so you can reuse your Dockerfile from that task. **Note that we have a new index.html file in this task so we need to build a new image that copies the correct file.**

### Build new image
```
docker build --tag dynamic-website .
```

### Run container
```
docker run --rm -p 8080:80 dynamic-website
```

## API
The code for the API we will use is in the [api](../api) folder.

This API should be run in a separate container. The API will listen to port 5000 so we need to expose port 5000 on the container on port 5000 on our system.

- **Write a Dockerfile that:**
1. Installs the requirements for the API
2. Runs the API

See the [README](../api/README.md) for the API code on how to do this.

- **Create an image from your Dockerfile using the `docker build` command:**
```
docker build --tag flask-api .
```

- **Start a container from the image using the `docker run` command:**
```
docker run --rm --publish 5000:5000 flask-api
```

You should now be able to view the website by opening http://localhost:8080 in a browser.

Can you see the value we got from the API? Try reloading the page and see if the value changes.
