# Generated by Django 3.0.8 on 2020-07-21 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200720_2255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='community',
        ),
        migrations.RemoveField(
            model_name='user',
            name='joined_at',
        ),
    ]
