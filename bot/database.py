import psycopg2
from modules import User, Msg
import os 

DJANGO_DB_USER = os.environ.get("DJANGO_DB_USER")
DJANGO_DB_NAME = os.environ.get("DJANGO_DB_NAME")
DJANGO_DB_PASSWORD = os.environ.get("DJANGO_DB_PASSWORD")
DJANGO_DB_PORT = os.environ.get("DJANGO_DB_PORT")


def is_inside_container():
    if os.path.exists('/.dockerenv'):
        return 1
    return 0

if is_inside_container():
    DATABASE_HOST = 'db'
else:
    DATABASE_HOST = 'localhost'


class Database():
    def __init__(self):
        self.conn = psycopg2.connect(
                f"host={DATABASE_HOST} port={DJANGO_DB_PORT} dbname={DJANGO_DB_NAME} user={DJANGO_DB_USER} password={DJANGO_DB_PASSWORD}") 
        self.curr = self.conn.cursor()

    def insert_message(self, message: Msg):
        print(self.curr.execute("INSERT INTO messages (text, user_id, direction, message_id) VALUES (%s, %s, %s, %s)",
            (message.text, message.user_id, message.direction, message.message_id)))
        self.conn.commit()

    def insert_user(self, user: User):
        self.curr.execute("SELECT tg_id FROM users WHERE tg_id=%s", (user.tg_id,))
        if len(self.curr.fetchall()) > 0:  
            return

        print(self.curr.execute("INSERT INTO users(tg_id, is_bot, username, first_name, last_name) VALUES (%s,%s,%s,%s,%s)",
            (user.tg_id, user.is_bot, user.username, user.first_name, user.last_name)))
        self.conn.commit()


# db.insert_user(User(394773843, False, 'eskislav', 'Viacheslav', 'Kozachok'))
# db.insert_message(Msg(1234))
