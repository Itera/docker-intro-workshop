from python:3.6

COPY requirements.txt .
COPY api.py .

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "api.py"]
