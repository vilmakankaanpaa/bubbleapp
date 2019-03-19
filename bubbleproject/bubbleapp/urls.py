from django.urls import path
from . import views
from django.urls import reverse_lazy
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
app_name = 'bubbleapp'
urlpatterns = [
  path('', views.index, name='index'),
  path('feed/<int:hashtag_id>/', views.detail, name='detail'),
  path('feed/delete_hashtag/<int:hashtag_id>/', views.delete_hashtag, name='delete_hashtag'),
  path('favourites/', views.favourites, name='favourites'),

  # user profile
  path('login/', LoginView.as_view(template_name='bubbleapp/login.html'), name='login'),
  path('logout/', LogoutView.as_view(template_name='bubbleapp/logout.html'), name='logout'),
  path('profile/', views.view_profile, name='view_profile'),
  path('profile/edit/', views.edit_profile, name='edit_profile'),
  path('register/', views.register, name='register'),
  path('profile/change-password/', views.change_password, name='change_password'),

  path('reset-password/', PasswordResetView.as_view(template_name='bubbleapp/reset_password.html', success_url= reverse_lazy('bubbleapp:password_reset_done'), email_template_name='bubbleapp/password_reset_email.html'), name='password_reset'),

  path('reset-password/done/', PasswordResetDoneView.as_view(template_name='bubbleapp/password_reset_done.html'), name='password_reset_done'),

  path('reset-password/confirm/<slug:uidb64>/<slug:token>', PasswordResetConfirmView.as_view(template_name='bubbleapp/password_reset_confirm.html', success_url=reverse_lazy('bubbleapp:password_reset_complete')), name='password_reset_confirm'),

  path('reset-password/complete/', PasswordResetCompleteView.as_view(template_name='bubbleapp/password_reset_complete.html'), name='password_reset_complete'),

  # brewerydb
  path('beers/', views.beers_view, name='beers')
]
