FROM python:3.6

RUN pip3 install jupyter

RUN mkdir /notebooks

COPY ./requirements.txt .

RUN pip3 install -r requirements.txt

EXPOSE 8888

CMD jupyter notebook --notebook-dir=/notebooks --ip=0.0.0.0 --port=8888 --allow-root
