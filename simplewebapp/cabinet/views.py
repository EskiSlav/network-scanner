import json
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse, HttpResponseBadRequest
import os
from cabinet.models import Users, Messages
import requests
from cabinet.forms import MessageForm
from urllib.parse import unquote

def is_inside_container():
    if os.path.exists('/.dockerenv'):
        return 1
    return 0


def cabinet(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login/')

    user_data_list = [ {'id': user.tg_id, 
                        'username': user.username, 
                        'first_name': user.first_name, 
                        'last_name': user.last_name } for user in Users.objects.all() ]
    
    
    form = MessageForm()
    return render(request, "cabinet.html", context={'users': user_data_list, 'form': form})
    
def send_messages(request, user_id):
    
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if not request.method == 'GET':
        return JsonResponse({'status': 'Invalid request'}, status=400)

    if not is_ajax:
        return HttpResponseBadRequest("Invalid request")

    data = {
        '0': [
            #data added here
        ]
    }
    
    for message in Messages.objects.filter(user_id=user_id):
        data['0'].append(
            {
                'user_id': message.user.tg_id,
                'text': message.text,
                'direction': message.direction,
                'message_id': message.message_id,
            }
        )
    
    return JsonResponse(data)


def send_message(request, user_id, text):

    if is_inside_container():
        host = "bot-sender"
    else:
        host = "localhost"

    url = f"http://{host}:8082/send_message/{user_id}/{text}"
    response = requests.get(url)
    if response.status_code == 200:
        user = Users.objects.filter(tg_id=user_id)[0]
        msg = Messages.objects.create(
            message_id=user.total_messages+1,
            text=text,
            user=user,
            direction="to"
        )
        msg.save()
    data = {
        'status': response.status_code, 
        'method': request.method 
    }
    return JsonResponse(data, status=response.status_code)

def send_message_POST(request):

    if is_inside_container():
        host = "bot-sender"
    else:
        host = "localhost"

    if request.method == "POST":
        POST_data = json.loads(request.body)
        text = POST_data['text']
        user_id = POST_data['user_id']
    
    url = f"http://{host}:8082/send_message/{user_id}/{text}"
    print(url)
    response = requests.get(url)
    if response.status_code == 200:
        user = Users.objects.filter(tg_id=user_id)[0]
        msg = Messages.objects.create(
            message_id=user.total_messages+1,
            text=unquote(text),
            user=user,
            direction="to"
        )
        msg.save()
    data = {
        'status': response.status_code, 
        'method': request.method 
    }
    return JsonResponse(data, status=response.status_code)