from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView

app_name = 'bubbleapp'
urlpatterns = [
  path('', views.index, name='index'),
  path('login/', LoginView.as_view(template_name='bubbleapp/login.html')),
]
