# Generated by Django 4.0.3 on 2022-08-13 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='slug',
        ),
    ]
