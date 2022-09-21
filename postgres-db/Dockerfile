FROM postgres:14.5-alpine

WORKDIR /opt/seed-data/

COPY seed.sql .
COPY my-postgres.conf /etc/postresql/postgresql.conf

# ENTRYPOINT [ "/docker-entrypoint-initdb.d/" ]
EXPOSE 5432

CMD ["postgres"]