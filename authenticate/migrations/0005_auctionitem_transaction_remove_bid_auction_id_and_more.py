# Generated by Django 4.1.3 on 2023-03-13 13:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0004_order_is_dispatched'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuctionItem',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=256)),
                ('item_description', models.TextField()),
                ('start_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('end_time', models.BooleanField(blank=True, default=False, null=True)),
                ('starting_price', models.FloatField(blank=True, default=100.0, null=True)),
                ('current_bid', models.FloatField(blank=True, null=True)),
                ('seller_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('transaction_id', models.AutoField(primary_key=True, serialize=False)),
                ('transaction_time', models.DateTimeField(auto_now_add=True)),
                ('transaction_amount', models.FloatField()),
                ('buyer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buyer_id_for_transaction', to=settings.AUTH_USER_MODEL)),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authenticate.auctionitem')),
                ('seller_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller_id_for_transaction', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='bid',
            name='Auction_id',
        ),
        migrations.RemoveField(
            model_name='sellingitem',
            name='is_auction_item',
        ),
        migrations.AddField(
            model_name='bid',
            name='bid_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bid',
            name='bid_price',
            field=models.FloatField(default=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='seller_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seller_id_for_order', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='sellingitem',
            name='item_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Auction',
        ),
        migrations.AddField(
            model_name='bid',
            name='auction_item_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authenticate.auctionitem'),
        ),
    ]
