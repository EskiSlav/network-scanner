import imp
from django.shortcuts import render
from django.http import HttpResponseRedirect


def cabinet(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login/')
    return render(request, "cabinet.html")

