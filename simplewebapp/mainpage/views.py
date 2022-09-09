import socket
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import LoginForm


def index(request):
    return redirect(f"http://localhost:8081/login")

def login(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/cabinet/')
    else:
        form = LoginForm()
    return render(request, 'login.html', { 'form': form })

def mainpage(request):
    return render(request, 'index.html')

