from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.cabinet, name='cabinet'),
    path('messages/user/<int:user_id>', views.send_messages, name='messages'),
    # path('send_message/<int:user_id>/<str:text>', views.send_message, name='send_message'),
    path('send_message/', views.send_message_POST, name='send_message_post'),
]