FROM python:3.7.5-alpine3.9
COPY . /app
WORKDIR /app
RUN apk update && apk add postgresql-dev gcc python2-dev musl-dev
RUN pip3 install -r requirements.txt
CMD python3 ./main.py