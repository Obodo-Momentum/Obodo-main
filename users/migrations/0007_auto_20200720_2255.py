# Generated by Django 3.0.8 on 2020-07-20 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200720_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='community',
            field=models.CharField(choices=[('Raleigh', 'Raleigh'), ('Durham', 'Durham'), ('Wake Forest', 'Wake Forest'), ('Chapel Hill', 'Chapel Hill'), ('Cary', 'Cary'), ('Apex/Holly Springs', 'Apex/Holly Springs'), ('Garner', 'Garner'), ('Clayton', 'Clayton'), ('Knightdale/Zebulon', 'Knightdale/Zebulon')], default='', max_length=55),
        ),
    ]
