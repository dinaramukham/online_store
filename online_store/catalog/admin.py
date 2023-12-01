from django.contrib import admin
from .models import  Category, Product
#admin.site.register(Category )
admin.site.register(Product )

@admin.register(Category )
class CategoryModelAdmin(admin.ModelAdmin  ):
    list_display = ('id','name_category',)