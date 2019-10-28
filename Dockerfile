FROM python:3.7-alpine
COPY . /app
WORKDIR /app
RUN apk update && apk add postgresql-dev gcc python2-dev
RUN pip install -r requirements.txt
CMD python ./main.py