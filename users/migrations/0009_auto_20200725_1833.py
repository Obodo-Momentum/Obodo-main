# Generated by Django 3.0.8 on 2020-07-25 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20200721_1356'),
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.CharField(choices=[('Raleigh', 'Raleigh'), ('Durham', 'Durham'), ('Wake Forest', 'Wake Forest'), ('Chapel Hill', 'Chapel Hill'), ('Cary', 'Cary'), ('Apex/Holly Springs', 'Apex/Holly Springs'), ('Garner', 'Garner'), ('Clayton', 'Clayton'), ('Knightdale/Zebulon', 'Knightdale/Zebulon')], max_length=55)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='community',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='users.Community'),
        ),
    ]
