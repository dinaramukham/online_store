from datetime import datetime

from django.db import models

# Create your models here.
class Product(models.Model  ):
    name=models.CharField(max_length= 30, default='')
    message=models.TextField(default='' )
    photo=models.ImageField(upload_to='static/')
    name_category=models.CharField(max_length= 30, default='')
    unit_price=models.IntegerField(null= True)
    date_of_creation=models.DateTimeField(null= True  )
    last_modified_date=models.DateTimeField(null= True)
    def __str__(self):
        return self.name
    class Meta():
        verbose_name='продукт'
        verbose_name_plural='продукты'
class Category(models.Model  ):
    name_category=models.CharField(max_length= 30,default='')
    message_category=models.TextField(default='')
    #craeted_at=models.TextField('none')
    def __str__(self):
        return self.name_category
    class Meta():
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
class Version(models.Model):
    product=models.ForeignKey('Product', on_delete=models.CASCADE)
    number_version=models.IntegerField()
    name_version=models.CharField(max_length=30)
    new=models.TextField()

    is_active=models.BooleanField(default=True)
    def __str__(self):
        return self.name_version


