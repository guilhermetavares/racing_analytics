FROM python:3

COPY ./requirements/ /requirements/
RUN pip install -r /requirements/base.txt

COPY ./tests $HOME/tests/
COPY ./* $HOME/app/
WORKDIR /app/
