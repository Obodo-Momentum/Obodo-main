# Generated by Django 3.0.8 on 2020-07-20 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('obodo', '0004_photo_member'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='member',
        ),
    ]
