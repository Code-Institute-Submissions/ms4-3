# Generated by Django 3.1.1 on 2020-10-28 22:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_auto_20201028_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review_rating',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(5)]),
        ),
    ]