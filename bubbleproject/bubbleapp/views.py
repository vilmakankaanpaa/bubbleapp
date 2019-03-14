from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader

from .models import Hashtag, Account

# Create your views here.

def detail(request, hashtag_id):
    hashtag = get_object_or_404(Hashtag, pk=hashtag_id)
    return render(request, 'bubbleapp/detail.html', {'hashtag': hashtag})

def feed(request):
    my_hashtags = Hashtag.objects.order_by('-add_date')
    args = { 'my_hashtags': my_hashtags}
    return render(request, 'bubbleapp/feed.html', args)

def index(request):
    return render(request, 'bubbleapp/index.html', {})

def profile(request):
    return render(request, 'bubbleapp/profile.html', {})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/bubbleapp')
    else:
        form = UserCreationForm()

        args = {'form': form}
        return render(request, 'bubbleapp/req_form.html', args)
