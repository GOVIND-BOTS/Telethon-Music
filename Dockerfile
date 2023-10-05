FROM python:3.9.7-slim-buster

RUN apt-get update && apt-get upgrade -y
RUN apt-get install git curl python3-pip -y
RUN pip3 install -U pip
RUN python3 -m pip install --upgrade pip

RUN apt-get install -y apt-transport-https
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs
RUN npm i -g npm

COPY . /app/
WORKDIR /app/

RUN pip3 install -U -r requirements.txt

CMD ["python3", "-m", "zaid"]
