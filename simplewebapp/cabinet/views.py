from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponseRedirect
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
    return render(request, "cabinet.html", context={'users': user_data_list})

