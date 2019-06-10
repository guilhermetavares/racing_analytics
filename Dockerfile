FROM python:3

ADD ./* $HOME/src/
WORKDIR /src/

ADD ./requirements/ /requirements/
RUN pip install -r /requirements/base.txt
