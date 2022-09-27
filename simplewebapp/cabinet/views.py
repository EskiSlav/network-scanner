from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse, HttpResponseBadRequest
import psycopg2
import os
from cabinet.models import Users, Messages

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
    
    return render(request, "cabinet.html", context={'users': user_data_list})


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

