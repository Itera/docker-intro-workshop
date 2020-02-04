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

## Question 1.1
The content changed because we mounted our folder into the container, so when we change something in our local folder the same changes are applied to the file system in the container.

## Question 1.2
The content did not change because we copied our `index.html` file into the container before changing it. If we want to use our changed file we would have to build a new image where we copy the new version of the file and run a new container using the updated image.
