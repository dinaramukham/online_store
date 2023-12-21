from django.contrib import admin
from .models import Category, Product, Version


# admin.site.register(Category )
@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_category')


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'name_category', 'unit_price', 'date_of_creation', 'last_modified_date',)
    list_filter = ('name_category',)
    search_fields = ('message', 'name',)


@admin.register(Version)
class VersionModelAdmin(admin.ModelAdmin):
    list_display = ('product', 'number_version', 'name_version', 'new', 'is_active',)
    list_filter = ('product', 'number_version', 'name_version', 'new', 'is_active',)
    search_fields=('product', 'number_version', 'name_version', 'new', 'is_active',)