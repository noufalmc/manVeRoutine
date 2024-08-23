FROM python:3.12

ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY . /code/

RUN pip install -r requirements.txt

