FROM ubuntu:18.04
RUN apt-get update -y
RUN apt-get install -y python3-pip python3 ffmpeg libsm6 libxext6
WORKDIR /iWebLens
COPY . .
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN rm requirement.txt
EXPOSE 5000
ENTRYPOINT [ "python3", "iWebLens_server.py" ]

