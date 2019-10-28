FROM python:3.6.9-alpine
COPY . /app
WORKDIR /app
RUN apk update && apk add postgresql-dev gcc python2-dev musl-de
RUN pip install -r requirements.txt
CMD python ./main.py