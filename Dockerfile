FROM python:3

ADD ./requirements/ /requirements/
RUN pip install -r /requirements/base.txt

ADD ./* $HOME/src/
WORKDIR /src/
