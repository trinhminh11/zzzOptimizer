# Generated by Django 4.2.14 on 2024-08-07 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_agentdatabase_realname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agentdatabase',
            name='icon',
            field=models.ImageField(default='', upload_to='media/agents/'),
        ),
    ]
