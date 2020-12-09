# Generated by Django 3.1.1 on 2020-12-09 22:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0010_remove_orderlineitem_order_linked_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='Linked_Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linked_product', models.CharField(blank=True, max_length=254, null=True)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='linked_product', to='checkout.order')),
            ],
        ),
    ]
