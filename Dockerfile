FROM python:3

ADD ./requirements/ /requirements/
RUN pip install -r /requirements/base.txt

ADD ./tests $HOME/tests/
ADD ./* $HOME/app/
WORKDIR /app/
