# Generated by Django 3.1.1 on 2021-01-24 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20210116_1629'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='linked_to_blog',
        ),
        migrations.AlterField(
            model_name='image_upload',
            name='sku',
            field=models.CharField(default='ae639a63-ac41-49bd-8431-0a90cc014681', max_length=254),
        ),
    ]
