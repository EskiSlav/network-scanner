FROM python:3.11.0rc2-alpine3.16

WORKDIR /opt/opinov8bot/

COPY . .

RUN apt update \
    && pip install --upgrade pip \
    && rm -rf env \
    && pip install -r requirements.txt

# ENTRYPOINT [ "docker-entrypoint.sh" ]

CMD python main.py

