FROM python:3.6-alpine3.6

ENV LANG C.UTF-8

RUN mkdir /app

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt