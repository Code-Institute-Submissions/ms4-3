# Generated by Django 3.1.1 on 2020-11-22 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_auto_20201122_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='number_of_pictures',
            field=models.IntegerField(default=0),
        ),
    ]