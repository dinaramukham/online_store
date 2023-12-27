from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from .forms import UserRegister, UserChangeProfile
from .models import User


# from online_store.online_store import settings


# Create your views here.
class UserCreateView(CreateView):
    model = User
    form_class = UserRegister
    template_name = 'users/register.html'
    success_url = reverse_lazy('product_list')

    def form_valid(self, form):
        new_email = form.save()
        send_mail(
            'Регистрауия прошла успешно!',
            'Добро пожаловать!',
            'empty_emailll@rambler.ru',
            [new_email.email],

        )
        return super().form_valid(form)


class ProfileUpdateView(UpdateView):
    model = User
    form_class = UserChangeProfile
    template_name = 'users/change.html'
    success_url = reverse_lazy('product_list')

    def get_object(self, queryset=None):
        return self.request.user


def get_new_password(request):
    new_password = User.objects.make_random_password()
    send_mail(
        'Смена пароля',
        f'Новый пароль: {new_password}',
        'empty_emailll@rambler.ru',
        [request.user.email],

    )
    request.user.set_password(new_password)
    return redirect(reverse('users_login'))
