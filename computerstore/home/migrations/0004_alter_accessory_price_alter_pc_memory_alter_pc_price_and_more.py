# Generated by Django 4.0.3 on 2022-08-15 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_accessory_slug_alter_pc_slug_alter_type_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessory',
            name='price',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pc',
            name='memory',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pc',
            name='price',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pc',
            name='ram',
            field=models.PositiveIntegerField(default=0),
        ),
    ]