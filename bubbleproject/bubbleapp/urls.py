from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'bubbleapp'
urlpatterns = [
  path('', views.index, name='index'),
  path('<int:hashtag_id>/', views.detail, name='detail'),
  path('feed/', views.feed, name='feed'),
  path('login/', LoginView.as_view(template_name='bubbleapp/login.html')),
  path('logout/', LogoutView.as_view(template_name='bubbleapp/logout.html')),
  path('profile/', views.view_profile, name='view_profile'),
  path('profile/edit/', views.edit_profile, name='edit_profile'),
  path('register/', views.register, name='register'),
]
