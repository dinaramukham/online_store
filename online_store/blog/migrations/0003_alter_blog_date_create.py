# Generated by Django 4.2.7 on 2023-12-10 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_create',
            field=models.IntegerField(default=2023),
        ),
    ]
