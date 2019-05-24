# Generated by Django 2.2 on 2019-05-09 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0003_auto_20190430_0615'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paymentmethod',
            old_name='available_balance',
            new_name='available_amount',
        ),
        migrations.RemoveField(
            model_name='paymentmethod',
            name='currency_name',
        ),
        migrations.AddField(
            model_name='paymentmethod',
            name='weight',
            field=models.CharField(blank=True, choices=[('Gram', 'Gram')], max_length=3, null=True),
        ),
    ]