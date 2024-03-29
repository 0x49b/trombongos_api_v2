# Generated by Django 3.2.12 on 2022-04-19 08:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0004_calendar_register'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='calendar',
            options={'ordering': ('season', 'from_date', 'from_time'), 'verbose_name': 'Kalender',
                     'verbose_name_plural': 'Kalender'},
        ),
        migrations.AlterField(
            model_name='calendar',
            name='from_time',
            field=models.TimeField(blank=True, null=True, verbose_name='From'),
        ),
    ]
