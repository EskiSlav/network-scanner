import psycopg
import asyncio
from modules import User, Msg
from async_class import AsyncClass

class Database():
     def __init__(self):
        self.conn = psycopg.connect(
                "host=localhost port=5432 dbname=db user=db_user password=fRt36viDyDhqc6a33qxH") 
        self.curr = self.conn.cursor()

     def insert_message(self, message: Msg):
        print(self.curr.execute("INSERT INTO messages (text, user_id, direction) VALUES (%s, %s, %s)",
            (message.text, message.user_id, message.direction)))


     def insert_user(self, user: User):
        print(self.curr.execute("INSERT INTO users(tg_id, is_bot, username, first_name, last_name) VALUES (%s,%s,%s,%s,%s)",
            (user.tg_id, user.is_bot, user.username, user.first_name, user.last_name)))


db = Database()
db.insert_user(User(394773843, False, 'eskislav', 'Viacheslav', 'Kozachok'))
# db.insert_message(Msg(1234))
# asyncio.run()