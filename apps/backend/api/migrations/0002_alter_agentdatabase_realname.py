# Generated by Django 4.2.14 on 2024-08-07 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agentdatabase',
            name='realName',
            field=models.CharField(default='', max_length=50, unique=True),
        ),
    ]