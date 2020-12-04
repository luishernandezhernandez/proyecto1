From python:3.6

MAINTAINER Luis Antonio Hernandez Hernandez "luanhh05@gmail.com"

EXPOSE 5000

WORKDIR /app

copy requeriments.txt /app

RUN pip install -r requeriments.txt

copy . /app

cmd python

