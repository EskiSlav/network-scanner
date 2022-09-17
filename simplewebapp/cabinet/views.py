from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
import psycopg2
import os

def is_inside_container():
    if os.path.exists('/.dockerenv'):
        return 1
    return 0

class DB:
    def __init__(self):
        host = "db" if is_inside_container() else "localhost"
        connection_str = "host={} port=5432 dbname=db user=db_user password=fRt36viDyDhqc6a33qxH".format(host)
        self.connection = psycopg2.connect(connection_str)
        self.cursor = self.connection.cursor()
    
    def get_data_for_user_side(self):
        sql = '''
        SELECT tg_id, username, first_name, last_name FROM users'''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_data_for_messages_side(self, user_id):
        sql = '''
        SELECT user_id, text, direction, message_id FROM messages WHERE user_id=%s '''
        self.cursor.execute(sql, (user_id,))
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()


def cabinet(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login/')
    
    db = DB()
    user_data_list = db.get_data_for_user_side()
    user_data_list = [ {'id': user[0], 
                        'username': user[1], 
                        'first_name': user[2], 
                        'last_name': user[3] } for user in user_data_list ]
    db.close()
    return render(request, "cabinet.html", context={'users': user_data_list})

def send_messages(request, user_id):
    data = {
        '0': [
            #data added here
        ]
    }
    # user_id = int(request.path.split('/')[-2])
    db = DB()
    messages_data_list = db.get_data_for_messages_side(user_id)
    for message in messages_data_list:
        data['0'].append(
            {
                'user_id': message[0],
                'text': message[1],
                'direction': message[2],
                'message_id': message[3],
            }
        )
    db.close()
    return JsonResponse(data)
