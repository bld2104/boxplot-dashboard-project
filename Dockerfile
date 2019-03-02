FROM python:3.6

WORKDIR /app

COPY . /app

RUN curl https://raw.githubusercontent.com/apex/apex/master/install.sh | sh

ENV AWS_ACCESS_KEY_ID *******************
ENV AWS_SECRET_ACCESS_KEY *******************
ENV AWS_REGION us-east-1

RUN echo 'SASHA echo RUN'

CMD apex deploy dashboard-update-date

