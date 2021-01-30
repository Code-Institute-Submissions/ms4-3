# Generated by Django 3.1.1 on 2021-01-30 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_auto_20210129_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_upload',
            name='sku',
            field=models.CharField(default='9e4024e2-00b8-4bd2-8f00-e96ca7cceb6e', max_length=254),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='default_county',
            field=models.CharField(blank=True, default='County', max_length=80),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='default_phone_number',
            field=models.CharField(blank=True, default='Phone Number', max_length=20),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='default_postcode',
            field=models.CharField(blank=True, default='Postcode', max_length=20),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='default_street_address1',
            field=models.CharField(blank=True, default='Street 1', max_length=80),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='default_street_address2',
            field=models.CharField(blank=True, default='Street 2', max_length=80),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='default_town_or_city',
            field=models.CharField(blank=True, default='Town or Ciry', max_length=40),
        ),
    ]