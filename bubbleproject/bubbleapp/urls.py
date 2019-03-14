from django.urls import path
from . import views
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

urlpatterns = [
  path('', views.index, name='index'),
  path('<int:hashtag_id>/', views.detail, name='detail'),
  path('feed/', views.feed, name='feed'),

  # user profile
  path('login/', LoginView.as_view(template_name='bubbleapp/login.html')),
  path('logout/', LogoutView.as_view(template_name='bubbleapp/logout.html')),
  path('profile/', views.view_profile, name='view_profile'),
  path('profile/edit/', views.edit_profile, name='edit_profile'),
  path('register/', views.register, name='register'),
  path('profile/change-password/', views.change_password,
    name='change_password'),
  path('reset-password/', PasswordResetView.as_view(),
    name='password_reset'),
  path('reset-password/done/', PasswordResetDoneView.as_view(),
    name='password_reset_done'),
  path('reset-password/confirm/<slug:uidb64>/<slug:token>',
    PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
  path('reset-password/complete/', PasswordResetCompleteView.as_view(),
    name='password_reset_complete')
]
