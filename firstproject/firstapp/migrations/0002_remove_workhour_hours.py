# Generated by Django 2.2 on 2019-04-10 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workhour',
            name='hours',
        ),
    ]
