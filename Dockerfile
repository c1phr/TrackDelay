FROM python:2.7
ADD . /track-delay
WORKDIR /track-delay
RUN pip install -r requirements.txt