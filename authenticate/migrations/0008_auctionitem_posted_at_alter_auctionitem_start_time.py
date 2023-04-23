# Generated by Django 4.1.3 on 2023-03-21 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0007_auctionitem_item_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionitem',
            name='posted_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='auctionitem',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
