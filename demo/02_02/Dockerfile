FROM alpine

RUN apk add --update python3 py3-pip

WORKDIR /app

COPY my_sleeping_script.py .

RUN mkdir pickle

CMD [ "python3", "-u", "./my_sleeping_script.py" ]
