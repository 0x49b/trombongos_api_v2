# Generated by Django 3.2.12 on 2022-04-19 08:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0003_auto_20220419_1009'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendar',
            name='register',
            field=models.IntegerField(choices=[(0, 'Gesamt'), (1, 'Bläser'), (2, 'Schläger')], default=0),
        ),
    ]
