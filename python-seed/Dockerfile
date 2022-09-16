FROM python:3.11.0rc2-alpine3.16

WORKDIR /opt/python-seed/

COPY . .

# RUN apk update
# RUN apk add libpq-dev gcc
# RUN ["python", "-m", "pip", "install", "--upgrade", "pip"]
# # RUN ["python", "-m", "pip", "install", "psycopg2-binary"]
# RUN ["python", "-m", "pip", "install", "psycopg2"]
# RUN ["python", "-m", "pip", "install", "faker"]

# ENTRYPOINT [ "docker-entrypoint.sh" ]
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev \
    && python -m pip install psycopg2 faker

CMD python seed.py seed

