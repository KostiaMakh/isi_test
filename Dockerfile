FROM python:3.11 as base
ENV PYTHONUNBUFFERED 1

ARG SECRET_KEY

RUN apt-get update && apt-get install -y gettext binutils libproj-dev gdal-bin
WORKDIR /usr/src/isi-test-api

RUN mkdir -p /usr/src/isi-test-api/static
RUN chmod -R +x /usr/src/isi-test-api/static

EXPOSE 8000

COPY ./requirements.txt /usr/src/isi-test-api
RUN pip install -r requirements.txt

COPY . /usr/src/isi-test-api
RUN chmod +x ./entrypoint.sh