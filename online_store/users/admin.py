from django.contrib import admin

from .models import User


# Register your models here.
@admin.register(User)
class UserModelAdmin(admin.ModelAdmin  ):
    list_display = ('email', 'phone', 'avatar', 'country',)
    list_filter = ('email', 'phone', 'avatar', 'country',)
    search_fields = ('email', 'phone', 'avatar', 'country',)

