# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from .views import login_view, register_user
from django.contrib.auth.views import LogoutView


# Password reset
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', login_view, name="login"),
    path('accounts/login/',login_view,name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    # Password reset views
    path('reset-password/',auth_views.PasswordResetView.as_view(template_name="accounts/password-reset.html"),name="reset_password"),
    path('reset-password-sent/',auth_views.PasswordResetDoneView.as_view(template_name="accounts/reset-password-sent.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="accounts/set-new-password.html"),name="password_reset_confirm"),
    path('reset-password-complete/',auth_views.PasswordResetCompleteView.as_view(template_name="accounts/reset-password-complete.html"),name="password_reset_complete"),
]

#"