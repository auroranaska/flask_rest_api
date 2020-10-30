FROM python:3-alpine

COPY . /code

WORKDIR /code

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

CMD [ "python3", "./app.py" ]