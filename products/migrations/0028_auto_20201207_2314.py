# Generated by Django 3.1.1 on 2020-12-07 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0027_auto_20201207_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_upload',
            name='sku',
            field=models.CharField(default='e766fe75-70af-4214-8ad7-f993451d79c8', max_length=254),
        ),
        migrations.AlterField(
            model_name='image_upload',
            name='user',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]