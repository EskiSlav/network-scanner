#!/bin/bash
set -e
export PGPASSWORD=$POSTGRES_PASSWORD;
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
  CREATE USER $APP_DB_USER WITH PASSWORD '$APP_DB_PASS';
  CREATE DATABASE $APP_DB_NAME;
  GRANT ALL PRIVILEGES ON DATABASE $APP_DB_NAME TO $APP_DB_USER;
  \connect $APP_DB_NAME $APP_DB_USER
  CREATE EXTENSION pg_trgm;
  BEGIN;
    BEGIN;

    CREATE TABLE IF NOT EXISTS public.users
    (
        id serial NOT NULL,
        tg_id bigint NOT NULL,
        is_bot boolean,
        username character varying(128),
        first_name character varying(64),
        last_name character varying(64),
        PRIMARY KEY (is_bot)
    );

    CREATE TABLE IF NOT EXISTS public.messages
    (
        id serial NOT NULL,
        text text NOT NULL,
        user_id bigint NOT NULL,
        direction character varying(6) NOT NULL,
        PRIMARY KEY (id)
    );

    ALTER TABLE IF EXISTS public.messages
        ADD CONSTRAINT user_id FOREIGN KEY (user_id)
        REFERENCES public.users (tg_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID;

    END;
  COMMIT;
EOSQL