# Generated by Django 3.1.1 on 2020-12-08 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_orderlineitem_lineitem_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlineitem',
            name='order_linked_products',
            field=models.CharField(default='', max_length=1000, null=True),
        ),
    ]
