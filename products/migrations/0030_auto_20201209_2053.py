# Generated by Django 3.1.1 on 2020-12-09 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0029_auto_20201208_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_upload',
            name='sku',
            field=models.CharField(default='1637636a-8232-4fbd-87de-f0977b1ff995', max_length=254),
        ),
    ]
