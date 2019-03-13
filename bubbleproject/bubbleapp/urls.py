from django.urls import path

from . import views

app_name = 'djangoapp'
urlpatterns = [
  path('', views.index, name='index'),
]
