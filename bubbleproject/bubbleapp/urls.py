from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'bubbleapp'
urlpatterns = [
  path('', views.index, name='index'),
  path('login/', LoginView.as_view(template_name='bubbleapp/login.html')),
  path('logout/', LogoutView.as_view(template_name='bubbleapp/logout.html')),
  path('register/', views.register, name='register'),
]
