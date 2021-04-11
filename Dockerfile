FROM ubuntu:18.04
RUN apt-get update -y && apt-get install -y python3-pip python3
COPY . /iWebLens
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
EXPOSE 5000

