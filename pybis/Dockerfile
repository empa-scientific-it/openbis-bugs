FROM python:3.10-slim-buster

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app  /app
WORKDIR /app
RUN chmod +x test.py
CMD ./test.py