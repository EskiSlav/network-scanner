from django.urls import path
from . import views

urlpatterns = [
    path('', views.cabinet, name='cabinet'),
]