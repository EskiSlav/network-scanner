FROM postgres:14.5-alpine

WORKDIR /opt/seed-data/

COPY my-postgres.conf /etc/postresql/postgresql.conf

EXPOSE 5432

CMD ["postgres"]