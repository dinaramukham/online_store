from django.db import models

# Create your models here.
class Product(models.Model  ):
    name=models.CharField(max_length= 30)
    message=models.TextField()
    photo=models.ImageField(upload_to='static/')
    name_category=models.CharField(max_length= 30)
    unit_price=models.IntegerField()
    date_of_creation=models.DateTimeField()
    last_modified_date=models.DateTimeField()
class Category(models.Model  ):
    name_category=models.CharField(max_length= 30)
    message_category=models.TextField()

