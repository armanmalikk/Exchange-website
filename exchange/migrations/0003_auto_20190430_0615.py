# Generated by Django 2.2 on 2019-04-30 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0002_paymentmethod_currency_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentmethod',
            name='currency_name',
            field=models.CharField(blank=True, choices=[('BDT', 'BDT'), ('USD', 'USD')], max_length=3, null=True),
        ),
    ]
