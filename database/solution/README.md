# Database solution

### Extending the `python:3.6` docker image
We want our image to have version 3.6 of python installed, so let's base our image from the official [python](https://hub.docker.com/_/python) image.
```
FROM python:3.6
```

## Copy our db script
```
COPY db.py .
```

## Install the `psycopg2` package
```
RUN pip3 install psycopg2
```

## Run the script
```
CMD python3 db.py
```
