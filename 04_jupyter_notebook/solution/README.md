# Jupyter notebook solution

## Extending the `python:3.6` docker image
We want our image to have version 3.6 of python installed, so let's base our image from the official [python](https://hub.docker.com/_/python) image.

```
FROM python:3.6
```

## Install Jupyter
```
RUN pip3 install jupyter
```

## Install other requirements
Copy requirements.txt file

```
COPY ./requirements.txt .
```
Install requirements
```
RUN pip3 install -r requirements.txt
```

## Create directory for our notebook files

```
RUN mkdir /notebooks
```

## Expose port 8888
```
EXPOSE 8888
```

## Start the jupyter notebook
```
CMD ["jupyter", "notebook", "--notebook-dir=/notebooks", "--ip=0.0.0.0", "--port=8888", "--allow-root"]
```
