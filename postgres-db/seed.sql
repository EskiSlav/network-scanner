DROP TABLE IF EXISTS messages;
DROP TABLE IF EXISTS users;

CREATE TABLE IF NOT EXISTS users
(
    id serial NOT NULL,
    tg_id bigint NOT NULL UNIQUE,
    is_bot boolean,
    username character varying(128),
    first_name character varying(64),
    last_name character varying(64),
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS messages
(
    id serial NOT NULL,
    message_id bigint NOT NULL UNIQUE,
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

INSERT INTO users(tg_id, is_bot, username, first_name, last_name) 
    VALUES (559986402, False, 'lookwiderr', 'Oleksandra', 'Chazova');
INSERT INTO users(tg_id, is_bot, username, first_name, last_name) 
    VALUES (394773843, False, 'eskislav', 'Viacheslav', 'Kozachok');