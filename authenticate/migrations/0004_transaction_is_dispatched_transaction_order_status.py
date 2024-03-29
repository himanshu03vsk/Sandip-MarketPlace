# Generated by Django 4.1.3 on 2023-06-06 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0003_transaction_address_transaction_payment_mode'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='is_dispatched',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='order_status',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
