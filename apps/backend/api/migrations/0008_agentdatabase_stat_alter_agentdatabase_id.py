# Generated by Django 4.2.14 on 2024-08-09 13:51

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_agentdatabase_rankicon'),
    ]

    operations = [
        migrations.AddField(
            model_name='agentdatabase',
            name='stat',
            field=models.JSONField(default={}),
        ),
        migrations.AlterField(
            model_name='agentdatabase',
            name='id',
            field=models.IntegerField(default=api.models.auto_increment, editable=False, primary_key=True, serialize=False),
        ),
    ]