from django.core.management.base   import BaseCommand
import json
from online_store.catalog import models

class Command(BaseCommand ):
    def handle(self, *args, **options):
        with open('catalog/fixtures/category.json') as file:
            info_category=json.load(file )
        info_str=[]
        for str in info_category:
            info_str.append(models.Category(**str["fields"]) )
        models.Category.objects.bulk_create(info_str)