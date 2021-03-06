# Generated by Django 2.2 on 2019-05-26 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0019_auto_20190522_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactionform',
            name='receiveFrom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='exchange_receive_from', to='exchange.PaymentMethod'),
        ),
        migrations.AlterField(
            model_name='transactionform',
            name='sendFrom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='exchange_send_from', to='exchange.PaymentMethod'),
        ),
    ]
