from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.urls import reverse

from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

from .models import FavouriteStyle, FavouriteCategory, Beer, Style, Category
from .forms import (
    RegistrationForm,
    EditProfileForm,
    FavouriteStyleForm,
    FavouriteCategoryForm
)
from .collector import getBeers

import datetime

# Create your views here.

def index(request):
    return render(request, 'bubbleapp/index.html', {})

def delete_favourite_style(request, style_id):

    fStyle = get_object_or_404(FavouriteStyle, pk=style_id)
    print(fStyle.beerStyle)

    if request.method == 'POST':

        fStyle.delete()
        return redirect('/bubbleapp/favourites/')

    else:
        args = { 'style': fStyle }
        return render(request, 'bubbleapp/delete_favourite.html', args)

def delete_favourite_category(request, category_id):

    fCategory = get_object_or_404(FavouriteCategory, pk=category_id)

    if request.method == 'POST':
        fCategory.delete()
        return redirect('/bubbleapp/favourites/')

    else:
        args = { 'category': fCategory }
        return render(request, 'bubbleapp/delete_favourite.html', args)

def favourites(request):

    if request.method == 'POST':
        styleForm = FavouriteStyleForm(request.POST)
        categoryForm = FavouriteCategoryForm(request.POST)

        if styleForm.is_valid():
            selected_style = styleForm.cleaned_data['beerStyle']
            style_object = Style.objects.get(styleName=selected_style)
            styleForm.save(request.user, style_object)

        if categoryForm.is_valid():
            selected_category = categoryForm.cleaned_data['beerCategory']
            category_object = Category.objects.get(name=selected_category)
            categoryForm.save(request.user, category_object)

        return redirect('/bubbleapp/favourites/')

    else:
        styles = FavouriteStyle.objects.filter(user=request.user)
        styleForm = FavouriteStyleForm()

        categories = FavouriteCategory.objects.filter(user=request.user)
        categoryForm = FavouriteCategoryForm()

        args = {
            'styles': styles,
            'styleForm': styleForm,
            'categories': categories,
            'categoryForm': categoryForm
        }
        return render(request, 'bubbleapp/favourites.html', args)

def beers_view(request):

    getBeers() # updates the database, should be done somewhere else
    args = {
        'beers': Beer.objects.all(),
        'styles': Style.objects.all(),
        'categories': Category.objects.all()
    }
    return render(request, 'bubbleapp/beers.html', args)

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
