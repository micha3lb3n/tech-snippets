# Generated by Django 2.0.7 on 2019-12-28 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('replies', '0002_auto_20191228_2016'),
    ]

    operations = [
        migrations.RenameField(
            model_name='replies',
            old_name='basComment',
            new_name='baesComment',
        ),
    ]
