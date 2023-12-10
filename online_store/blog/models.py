from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=30)
    slug = models.CharField(max_length=150)
    message = models.TextField(default='')
    photo = models.ImageField(upload_to='media/')
    date_create = models.IntegerField(default= 2023)
    published = models.BooleanField(default=True)
    views_count = models.IntegerField(default=0)
    def __str__(self):
        return self.title