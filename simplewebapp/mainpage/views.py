import socket
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout

def index(request):
    return redirect(f"http://localhost:8081/login")

def login_view(request):
    message = ""

    if request.user.is_authenticated:
        return HttpResponseRedirect('/cabinet/')
        
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/cabinet/')
            else:
                message = "Invalid login or password"

    form = LoginForm()
    return render(request, 'login.html', { 'form': form , 'message': message})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def mainpage(request):
    return render(request, 'index.html')

