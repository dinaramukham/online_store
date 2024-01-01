from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .apps import UsersConfig
from .views import UserCreateView, get_new_password

app_name=UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='users_login'),
    path('logout/', LogoutView.as_view(), name='users_logout'),
    path('register/', UserCreateView.as_view(), name='users_register'),
    #path('profile/', ProfileUpdateView.as_view(), name='users_changer'),
    path('password/', get_new_password, name='users_password'),
]
