# Generated by Django 3.1.1 on 2021-01-29 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20210128_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_upload',
            name='image',
            field=models.ImageField(upload_to='media/images'),
        ),
        migrations.AlterField(
            model_name='image_upload',
            name='sku',
            field=models.CharField(default='1eaf4bc0-0242-4809-92b3-24e62debaa88', max_length=254),
        ),
    ]
