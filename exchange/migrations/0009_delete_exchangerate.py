# Generated by Django 2.2 on 2019-05-15 05:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0008_exchangerate'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ExchangeRate',
        ),
    ]
