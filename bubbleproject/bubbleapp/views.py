from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

from .models import Hashtag, Account
from .forms import (
    RegistrationForm,
    EditProfileForm,
    HashtagForm
)

import datetime

# Create your views here.

def index(request):
    return render(request, 'bubbleapp/index.html', {})

@login_required
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

            return redirect('/bubbleapp/feed/settings')

    else:
        form = HashtagForm(initial=data)
        args = { 'form': form }
        return render(request, 'bubbleapp/detail.html', args)

@login_required
def delete_hashtag(request, hashtag_id):
    hashtag = get_object_or_404(Hashtag, pk=hashtag_id)
    if request.method == 'POST':
        hashtag.delete()
        return redirect('/bubbleapp/feed/settings')
    else:
        args = { 'hashtag': hashtag }
        return render(request, 'bubbleapp/delete_hashtag.html', args)

@login_required
def feed_view(request):
    return render(request, 'bubbleapp/feed.html', {})

@login_required
def feed_settings(request):

    if request.method == 'POST':
        form = HashtagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/bubbleapp/feed/settings')

    else:
        my_hashtags = Hashtag.objects.order_by('-modified')
        form = HashtagForm()
        args = {
            'my_hashtags': my_hashtags,
            'form': form
        }
        return render(request, 'bubbleapp/feed_settings.html', args)

# Account management views

@login_required
def view_profile(request):
    args = {'user': request.user}
    return render(request, 'bubbleapp/profile.html', args)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/bubbleapp/profile')

    else:
        form = EditProfileForm(instance=request.user)
        return render(request, 'bubbleapp/edit_profile.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/bubbleapp')
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'bubbleapp/req_form.html', args)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/bubbleapp/profile')
        else:
            return redirect('/bubbleapp/profile/change-password')

    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'bubbleapp/change_password.html', args)
