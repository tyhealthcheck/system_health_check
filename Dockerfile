FROM ubuntu:latest

RUN apt update
RUN apt install python3 -y
RUN apt install python3-psutil -y

WORKDIR /home/ubuntu/ty_healthcheck

COPY ty_system_healthcheck.py ./

CMD [ "python3", "./ty_system_healthcheck.py"]
