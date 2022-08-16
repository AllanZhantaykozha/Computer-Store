# Generated by Django 4.0.3 on 2022-08-14 14:09

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_news_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessory',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='title'),
        ),
        migrations.AlterField(
            model_name='pc',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='title'),
        ),
        migrations.AlterField(
            model_name='type',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='title'),
        ),
    ]
