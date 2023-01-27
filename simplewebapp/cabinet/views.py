import json
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse, HttpResponseBadRequest
import os
import requests
from .forms import ScanForm
from urllib.parse import unquote


def is_inside_container():
    if os.path.exists('/.dockerenv'):
        return 1
    return 0


def cabinet(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login/')

        
    form = ScanForm()
    return render(request, "cabinet.html", context={'form': form})
