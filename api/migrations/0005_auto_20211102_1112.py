# Generated by Django 3.2.9 on 2021-11-02 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_transport'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transport',
            options={'ordering': ('id',), 'verbose_name': 'Transport', 'verbose_name_plural': 'Transporte'},
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('date', models.DateField()),
                ('ca_makeup', models.BooleanField(default=False)),
                ('makeup', models.TimeField(null=True)),
                ('warehouse', models.TimeField(null=True)),
                ('sun', models.TimeField(null=True)),
                ('gathering', models.TimeField()),
                ('ca_play', models.BooleanField(default=False)),
                ('play', models.TimeField()),
                ('trailer', models.CharField(blank=True, max_length=256, null=True)),
                ('information', models.TextField(blank=True, null=True)),
                ('public', models.BooleanField(default=True)),
                ('active', models.BooleanField(default=True)),
                ('fix', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.category')),
                ('evening', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.evening')),
                ('transport', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.transport')),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
        ),
    ]
