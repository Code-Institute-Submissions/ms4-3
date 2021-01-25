# Generated by Django 3.1.1 on 2021-01-25 21:27

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentreadytodownload',
            name='name',
            field=models.CharField(blank=True, default='Purchase', max_length=254),
        ),
        migrations.AlterField(
            model_name='contentreadytodownload',
            name='user',
            field=models.CharField(blank=True, default='Anonymous', max_length=254),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='default_country',
            field=django_countries.fields.CountryField(blank=True, default='UK', max_length=2),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='default_county',
            field=models.CharField(blank=True, default='*', max_length=80),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='default_phone_number',
            field=models.CharField(blank=True, default='*', max_length=20),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='default_postcode',
            field=models.CharField(blank=True, default='*', max_length=20),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='default_street_address1',
            field=models.CharField(blank=True, default='*', max_length=80),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='default_street_address2',
            field=models.CharField(blank=True, default='*', max_length=80),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='default_town_or_city',
            field=models.CharField(blank=True, default='*', max_length=40),
        ),
    ]
