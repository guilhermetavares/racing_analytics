FROM python:3

RUN mkdir -p ~/test
ADD script.py /

RUN pip install pystrich
