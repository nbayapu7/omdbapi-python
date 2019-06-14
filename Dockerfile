FROM ubuntu:latest
LABEL maintainer="nlbayapu@gmail.com"

RUN apt-get update
RUN apt-get install python python-pip -y
RUN pip install omdb
ADD ./omdbapi.py /root
USER root
WORKDIR /root
ENV OMDB_API_KEY xxxxxxx


CMD ["/bin/bash"]

