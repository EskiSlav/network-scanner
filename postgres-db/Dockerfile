FROM postgres:14.5-alpine

WORKDIR /opt/seed-data/

COPY seed.sql .

EXPOSE 5432

CMD ["postgres"]