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
    EditProfileForm
)

# Create your views here.

@login_required
def detail(request, hashtag_id):
    hashtag = get_object_or_404(Hashtag, pk=hashtag_id)
    return render(request, 'bubbleapp/detail.html', {'hashtag': hashtag})

@login_required
def feed(request):
    my_hashtags = Hashtag.objects.order_by('-add_date')
    args = { 'my_hashtags': my_hashtags}
    return render(request, 'bubbleapp/feed.html', args)

def index(request):
    return render(request, 'bubbleapp/index.html', {})

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
        args = {'form': form}
        return render(request, 'bubbleapp/edit_profile.html', args)

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
