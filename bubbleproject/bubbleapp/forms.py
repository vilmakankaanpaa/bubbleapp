from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import FavouriteStyle, FavouriteCategory, Style, Category

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password'
        )

class FavouriteStyleForm(forms.ModelForm):
    beerStyle = forms.ModelChoiceField(queryset=Style.objects.all())

    class Meta:
        model = FavouriteStyle
        fields = ['beerStyle']

    def save(self, user, style):
        f_style = FavouriteStyle(user=user, beerStyle=style)
        f_style.save()

        return f_style

class FavouriteCategoryForm(forms.ModelForm):
    beerCategory = forms.ModelChoiceField(queryset=Category.objects.all())

    class Meta:
        model = FavouriteCategory
        fields = ['beerCategory']

    def save(self, user, category):
        f_category = FavouriteCategory(user=user, beerCategory=category)
        f_category.save()

        return f_category
