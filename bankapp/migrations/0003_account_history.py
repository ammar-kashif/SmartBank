# Generated by Django 3.0.8 on 2020-07-26 15:49

import bankapp.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0002_auto_20200721_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='history',
            field=bankapp.models.ListField(blank=True),
        ),
    ]