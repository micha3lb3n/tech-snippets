# Generated by Django 2.0.7 on 2019-12-22 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20191222_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
