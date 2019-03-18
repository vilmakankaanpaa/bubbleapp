from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.urls import reverse

from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

from .models import Hashtag, Account, Beer, Style, Category
from .forms import (
    RegistrationForm,
    EditProfileForm,
    HashtagForm
)
from .collector import getBeers

import datetime

# Create your views here.

def index(request):
    return render(request, 'bubbleapp/index.html', {})

def detail(request, hashtag_id):

    hashtag = get_object_or_404(Hashtag, pk=hashtag_id)
    data = {
        'name': hashtag.name,
        'hashtag': hashtag.hashtag
    }
    if request.method == 'POST':
        form = HashtagForm(request.POST, initial=data)
        if form.is_valid():
            if form.has_changed():
                hashtag.name = form.cleaned_data['name']
                hashtag.hashtag = form.cleaned_data['hashtag']
                hashtag.modified = datetime.datetime.now()
                hashtag.save()

            return redirect(reverse('bubbleapp:feed_settings').lstrip('/'))

    else:
        form = HashtagForm(initial=data)
        args = { 'form': form }
        return render(request, 'bubbleapp/detail.html', args)

def delete_hashtag(request, hashtag_id):
    hashtag = get_object_or_404(Hashtag, pk=hashtag_id)
    if request.method == 'POST':
        hashtag.delete()
        return redirect(reverse('bubbleapp:feed:settings').lstrip('/'))
    else:
        args = { 'hashtag': hashtag }
        return render(request, 'bubbleapp/delete_hashtag.html', args)

def feed_view(request):
    return render(request, 'bubbleapp/feed.html', {})

def feed_settings(request):

    if request.method == 'POST':
        form = HashtagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('bubbleapp:feed_settings').lstrip('/'))

    else:
        my_hashtags = Hashtag.objects.order_by('-modified')
        form = HashtagForm()
        args = {
            'my_hashtags': my_hashtags,
            'form': form
        }
        return render(request, 'bubbleapp/feed_settings.html', args)

# Account management views

def view_profile(request):
    args = {'user': request.user}
    return render(request, 'bubbleapp/profile.html', args)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('bubbleapp:profile').lstrip('/'))

    else:
        form = EditProfileForm(instance=request.user)
        return render(request, 'bubbleapp/edit_profile.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('bubbleapp:index'))
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'bubbleapp/req_form.html', args)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('bubbleapp:profile').lstrip('/'))
        else:
            return redirect(reverse('bubbleapp:change_password').lstrip('/'))

    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'bubbleapp/change_password.html', args)

def beers_view(request):

    getBeers() # updates the database, should be done somewhere else
    args = {
        'beers': Beer.objects.all(),
        'styles': Style.objects.all(),
        'categories': Category.objects.all()
    }
    return render(request, 'bubbleapp/beers.html', args)
