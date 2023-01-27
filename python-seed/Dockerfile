FROM python:3.11.0rc2-alpine3.16

WORKDIR /opt/python-seed/

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev 

COPY requirements.txt .

RUN python -m pip install -r requirements.txt

COPY . .

CMD python seed.py seed

