import requests
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'bubbleapp/index.html', {})

def login(request):
    return render(request, 'bubbleapp/login.html', {})