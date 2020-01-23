# Data Science using a jupyter notebook

In this task we will create a Docker image we can use to run a jupyter kernel that can run our notebooks.

We will use the `python:3.6` base image for this task.

## Install Jupyter
In order to run our notebooks we need to install jupyter on our image. We can install it using the python package installer:
```
pip3 install jupyter
```

## Install other requirements
Our notebook code will need some other requirements as well. These are listed in the requirements.txt file. We can install them using the following command:
```
pip3 install -r requirements.txt
```

Note that you will have to copy the `requirements.txt` into the container before you run the command.

## Creating a folder for our notebooks
We will mount our notebooks into the container so first we need to create the folder:
```
mkdir notebooks
```

## Starting the jupyter kernel
The final command of our image is to start the jupytern kernel. This can be done with the command:
```
jupyter notebook --notebook-dir=/notebooks --ip=0.0.0.0 --port=8888 --allow-root
```

## Start the jupyter kernel in a container
In order to access our notebooks we need to mount our local `/notebooks` folder into the `/notebooks` folder in our container.

We also need to access the kernel on port `8888`.

We can achieve both these goals by running the command:

```
docker run --publish 8888:8888 -v $(pwd)/notebooks:/notebooks -it jupyter-notebook
```

## Do some data science!
We should now be able to access our notebook.

You should see an URL that looks like this in the container output:
```
http://127.0.0.1:8888/?token=95ce0cf993041fd5bfdab43c1e04be66dafa0b1be69e1b53
```

Open it in a browser and you should be able to see our notebook.

Try solving the first task by pasting the the following code into the cell:
```python
import pandas as pd
import random

rows = 20
columns = 10

min_n = 0
max_n = 100

column_names = [f'column_{n}' for n in range(10)]

l1 = [[random.randint(min_n, max_n) for i in range(rows)] for c in range(columns)]

d1 = dict(zip(column_names, l1))

df1 = pd.DataFrame(d1)

df1
```
