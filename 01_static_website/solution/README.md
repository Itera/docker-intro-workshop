## Extending the `nginx` docker image
We want to extend the `nginx` Docker image. We can do this with the `FROM` command like this:
```
FROM nginx
```

## Copying our webpage
We then want to add our webpage to the `/usr/share/nginx/html/` folder in the image. We can do this using the `COPY` command like this:
```
COPY index.html /usr/share/nginx/html
```