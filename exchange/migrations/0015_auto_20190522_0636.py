# Generated by Django 2.2 on 2019-05-22 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0014_transactionform_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactionform',
            name='phone',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='transactionform',
            name='sendAmount',
            field=models.CharField(max_length=100),
        ),
    ]