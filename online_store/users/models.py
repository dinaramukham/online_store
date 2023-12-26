from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}


# Create your models here.
class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True)
    phone = models.IntegerField(**NULLABLE )
    avatar = models.ImageField(upload_to='media/', **NULLABLE)
    country = models.CharField(max_length=150, **NULLABLE)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []