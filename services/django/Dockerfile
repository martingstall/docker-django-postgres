# pull official base image
FROM python:3.8.1-slim-buster

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /usr/src/app

# copy project
COPY . /usr/src/app/

# install system dependencies
RUN apt-get update && apt-get install -y netcat

RUN apt-get install -y nodejs
RUN apt-get install -y npm

# How to use this here?
#RUN npm install

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# run entrypoint.sh
#ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
