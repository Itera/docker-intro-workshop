# Dynamic website solution

## Website
We can reuse our solution from the first task in order to serve the webstie.

### Extending the `nginx` docker image
We want to extend the `nginx` Docker image. We can do this with the `FROM` command like this:
```
FROM nginx
```

### Copying our webpage
We then want to add our webpage to the `/usr/share/nginx/html/` folder in the image. We can do this using the `COPY` command like this:
```
COPY index.html /usr/share/nginx/html
```

## API
### Extending the `python:3.6` docker image
We want our image to have version 3.6 of python installed, so let's base our image from the official [python](https://hub.docker.com/_/python) image.
```
FROM python:3.6
```

### Copying API files
This API uses some 3rd party libraries, so we need to copy the list of requirements as well as the source code.

```
COPY requirements.txt .
COPY api.py .
```

### Installing requirements
Before we can start our API we need to install the requirements

```
RUN pip3 install -r requirements.txt
```

### Run our API
Finally we can run our API

```
ENTRYPOINT ["python3", "api.py"]
```
