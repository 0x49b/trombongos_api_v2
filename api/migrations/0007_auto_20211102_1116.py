# Generated by Django 3.2.9 on 2021-11-02 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20211102_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='sun',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='warehouse',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
