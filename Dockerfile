FROM python:3.8.0-alpine


MAINTAINER Tobias Moeller

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh /app/entrypoint.sh

# copy project
COPY . /app

# run entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]
