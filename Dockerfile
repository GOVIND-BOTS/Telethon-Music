FROM python:3.9.7-slim-buster

RUN apt-get update && apt-get upgrade -y

RUN pip3 install -U pip

RUN apt-get install -y apt-transport-https
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs

COPY . /app/
WORKDIR /app/

RUN pip3 install -U -r requirements.txt
RUN npm install -g npm@latest
RUN pip3 install zaid

CMD ["python3", "-m", "zaid"]
