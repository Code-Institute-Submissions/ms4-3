# Generated by Django 3.1.1 on 2020-11-22 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_image_upload'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image_upload',
            name='time',
        ),
        migrations.AddField(
            model_name='image_upload',
            name='user_upload_image_file_path',
            field=models.CharField(default='not found', max_length=200),
        ),
    ]
