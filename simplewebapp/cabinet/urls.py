from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.cabinet, name='cabinet'),
    path('messages/user/<int:user_id>', views.send_messages, name='messages'),
]