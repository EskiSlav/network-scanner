FROM python:3.11.0rc2-alpine3.16

WORKDIR /opt/opinov8bot/

COPY . .

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev \
    && python -m pip install --upgrade pip \
    && python -m pip install psycopg2 faker django

# ENTRYPOINT [ "docker-entrypoint.sh" ]
ENV DJANGO_DB_USER=db_user
ENV DJANGO_DB_NAME=db
ENV DJANGO_DB_PASSWORD=password
ENV DJANGO_DB_PORT=5432

CMD python ./manage.py runserver 8081

