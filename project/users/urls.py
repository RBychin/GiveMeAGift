from django.conf import settings
from django.urls import path, include
from django.contrib.auth.views import LoginView

from users import views

app_name = 'user'

urlpatterns = [
    path(
        'login/',
        LoginView.as_view(
            template_name='users/login.html'
        ), name='login'),
    path(
        'login/',
        LoginView.as_view(
            template_name='users/login.html'
        ), name='login'),
    path(
            'signup/',
            views.SignUp.as_view(),
            name='signup'
        ),
    ]

