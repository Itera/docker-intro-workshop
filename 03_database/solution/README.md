# Database solution

## Extending the `python:3.6` docker image
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
CMD ["python3" "db.py"]
```

## Question 3.1
Our container is attempting to reach the database on localhost by default, but the database is running in a different container, so without setting up some connection between the containers there is no database available. If we started the database in the same container as the script we would have been able to connect to it.

## Question 3.2
In the previous task there was no communication between the containers. All the communication was between our browser and the containers. First our browser fetched a website from the webserver, then it fetched some values from the API.

## Question 3.3
The output should change for each time because the db-script adds new values each time it is run and it connects to the same database each time.

## Question 3.4
The output should have been reset since last time, since we created a new database container and the previous state was lost. If we just stop and start the existing container instead of creating a new one then we would have kept the state.
