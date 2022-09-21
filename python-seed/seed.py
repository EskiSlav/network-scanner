import random
from sys import argv, stdout
from time import sleep
from typing import OrderedDict
import psycopg2
from faker import Faker
import logging
import os

logging.basicConfig(level=logging.DEBUG, stream=stdout)

faker = Faker('en')

def is_inside_container():
    if os.path.exists('/.dockerenv'):
        return 1
    return 0


class PostgreSeeder:

    def __init__(self):
        host = "db" if is_inside_container() else "localhost"
        connection_str = "host={} port=5432 dbname=db user=db_user password=fRt36viDyDhqc6a33qxH".format(host)
        def _again(n=0):
            try:
                if n == 10:
                    exit(1)
                sleep(1)
                n += 1
                self.connection = psycopg2.connect(connection_str)
            except:
                _again(n)
        _again()
        self.cursor = self.connection.cursor()

    def create_user_table(self):
        sql = '''
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
        '''
        self.cursor.execute(sql)
        self.connection.commit()

    def create_messages_table(self):
        sql = '''
            CREATE TABLE IF NOT EXISTS messages
            (
                id serial NOT NULL,
                message_id bigint NOT NULL UNIQUE,
                text text NOT NULL,
                user_id bigint NOT NULL,
                direction character varying(6) NOT NULL,
                PRIMARY KEY (id)
            );
        '''
        self.cursor.execute(sql)
        self.connection.commit()

    def create_messages_foreign_keys(self):
        sql = '''
            ALTER TABLE IF EXISTS messages
            ADD CONSTRAINT user_id FOREIGN KEY (user_id)
            REFERENCES users (tg_id) MATCH SIMPLE
            ON UPDATE NO ACTION
            ON DELETE NO ACTION
            NOT VALID;
        '''
        self.cursor.execute(sql)
        self.connection.commit()

    def create_all_tables(self):
        self.create_user_table()
        self.create_messages_table()
        self.create_messages_foreign_keys()

    def insert_users(self, users_number=300):
        for _ in range(users_number):
            sql = '''
            INSERT INTO users(tg_id, is_bot, username, first_name, last_name) 
            VALUES (%s,%s,%s,%s,%s)
            '''
            user_data = OrderedDict(
                tg_id = random.randint(100000000, 1000000000),
                is_bot = faker.boolean(chance_of_getting_true=2),
                username = faker.sentence(nb_words=1)[:-1],
                first_name = faker.sentence(nb_words=1)[:-1],
                last_name = faker.sentence(nb_words=1)[:-1],
            )
            args = tuple(user_data.values())
            self.cursor.execute(sql, args)
            
    def insert_messages(self, messages_number=1200):
        sql = '''
        SELECT tg_id FROM users;
        '''
        self.cursor.execute(sql)
        
        user_tg_ids = self.cursor.fetchall()
        print(user_tg_ids[:10])
        user_tg_ids = [ int(x[0]) for x in user_tg_ids ]
        directions = ["from", "to"]
        
        sql = '''
            INSERT INTO messages(message_id, text, user_id, direction) VALUES (%s, %s, %s, %s)
        '''
        for _ in range(messages_number):
            message_data = OrderedDict(
                message_id = random.randint(100000000, 1000000000),
                text = faker.sentence(nb_words=random.randint(4,12)),
                user_id = random.choice(user_tg_ids),
                direction = random.choice(directions),
            )
            args = tuple(message_data.values())
            self.cursor.execute(sql, args)
    
    def insert_data(self):
        self.insert_users()
        self.insert_messages()
        self.connection.commit()
    
    def seed(self):
        print("Clearing old data...")
        self.drop_all_tables()
        print("Start seeding...")
        self.create_all_tables()
        self.insert_data()

        self.connection.commit()
        self.cursor.close()
        self.connection.close()
        print("Done")
        

    def drop_user_table(self):
        self.cursor.execute('DROP TABLE IF EXISTS users;')

    def drop_messages_table(self):
        self.cursor.execute('DROP TABLE IF EXISTS users CASCADE ;')
    
    def drop_all_tables(self):
        self.drop_messages_table()
        self.drop_user_table()


def main():
    ps = PostgreSeeder()
    options = {
        'create_tables': ps.create_all_tables,
        'seed': ps.seed,
        'insert_data': ps.insert_data,
    }

    options[argv[1]]()


if __name__ == '__main__':
    main()