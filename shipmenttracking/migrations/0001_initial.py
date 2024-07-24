# Generated by Django 4.1.3 on 2022-11-29 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='shipmentTrack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trackingCode', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Tracking Code',
            },
        ),
    ]