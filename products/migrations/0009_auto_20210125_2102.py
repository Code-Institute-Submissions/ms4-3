# Generated by Django 3.1.1 on 2021-01-25 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20210125_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_upload',
            name='sku',
            field=models.CharField(default='e9c80195-429e-477e-a70e-9e7d34f12360', max_length=254),
        ),
    ]
