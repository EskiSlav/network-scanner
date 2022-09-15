#!/bin/bash
set -e
export PGPASSWORD=$POSTGRES_PASSWORD;
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
  CREATE USER $APP_DB_USER WITH PASSWORD '$APP_DB_PASS';
  CREATE DATABASE $APP_DB_NAME;
  GRANT ALL PRIVILEGES ON DATABASE $APP_DB_NAME TO $APP_DB_USER;
  \connect $APP_DB_NAME $APP_DB_USER
  CREATE EXTENSION pg_trgm;
  
  DROP TABLE IF EXISTS users;
  DROP TABLE IF EXISTS messages;

  CREATE TABLE IF NOT EXISTS users
  (
      id serial NOT NULL,
      tg_id bigint NOT NULL UNIQUE,
      is_bot boolean,
      username character varying(128),
      first_name character varying(64),
      last_name character varying(64),
      PRIMARY KEY (is_bot)
  );

  CREATE TABLE IF NOT EXISTS messages
  (
      id serial NOT NULL,
      message_id bigint NOT NULL UNIQUE
      text text NOT NULL,
      user_id bigint NOT NULL,
      direction character varying(6) NOT NULL,
      PRIMARY KEY (id)
  );

  ALTER TABLE IF EXISTS messages
      ADD CONSTRAINT user_id FOREIGN KEY (user_id)
      REFERENCES users (tg_id) MATCH SIMPLE
      ON UPDATE NO ACTION
      ON DELETE NO ACTION
      NOT VALID;

  INSERT INTO users VALUES(559986402, False, Oleksandra, Chazova, lookwiderr)
  INSERT INTO users VALUES(394773843, False, Viacheslav, Kozachok, eskislav)

EOSQL

# OrderedDict([('user_id', 559986402), ('text', 'Hi, businka Viacheslav EchoBot!')])
# OrderedDict([('user_id', 394773843), ('text', 'іва')])

