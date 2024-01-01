from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User


class UserRegister(UserCreationForm):
    def __init__(self, *args, **kwargs ):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
    class Meta:
        model=User
        fields=('email', 'password', 'password2',)
class UserChangeProfile(UserChangeForm):
    def __init__(self, *args, **kwargs ):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
    class Meta:
        model=User
        fields='__all__'

