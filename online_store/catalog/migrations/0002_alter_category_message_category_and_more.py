# Generated by Django 4.2.7 on 2023-12-01 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='message_category',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='category',
            name='name_category',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_of_creation',
            field=models.DateTimeField(default=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='last_modified_date',
            field=models.DateTimeField(default=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='message',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='name_category',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='unit_price',
            field=models.IntegerField(default=''),
        ),
    ]
