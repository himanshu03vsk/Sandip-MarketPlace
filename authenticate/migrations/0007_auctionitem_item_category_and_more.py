# Generated by Django 4.1.3 on 2023-03-14 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0006_alter_auctionitem_end_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionitem',
            name='item_category',
            field=models.CharField(blank=True, choices=[('art', 'Art'), ('antiques', 'Antiques'), ('books & magazines', 'Books & Magazines'), ('cameras & photo', 'Cameras & Photo'), ('cell phones & accessories', 'Cell Phones & Accessories'), ('clothing, shoes & accessories', 'Clothing, Shoes & Accessories'), ('coins & paper money', 'Coins & Paper Money'), ('collectibles', 'Collectibles'), ('computers/tablets & networking', 'Computers/Tablets & Networking'), ('consumer electronics', 'Consumer Electronics'), ('crafts', 'Crafts'), ('dolls & bears', 'Dolls & Bears'), ('everything else', 'Everything Else'), ('gift cards & coupons', 'Gift Cards & Coupons'), ('health & beauty', 'Health & Beauty'), ('jewelry & watches', 'Jewelry & Watches'), ('music', 'Music'), ('musical instruments & gear', 'Musical Instruments & Gear'), ('pet supplies', 'Pet Supplies'), ('pottery & glass', 'Pottery & Glass'), ('sporting goods', 'Sporting Goods'), ('stamps', 'Stamps'), ('tickets & experiences', 'Tickets & Experiences'), ('toys & hobbies', 'Toys & Hobbies'), ('video games & consoles', 'Video Games & Consoles')], max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='sellingitem',
            name='item_category',
            field=models.CharField(blank=True, choices=[('art', 'Art'), ('antiques', 'Antiques'), ('books & magazines', 'Books & Magazines'), ('cameras & photo', 'Cameras & Photo'), ('cell phones & accessories', 'Cell Phones & Accessories'), ('clothing, shoes & accessories', 'Clothing, Shoes & Accessories'), ('coins & paper money', 'Coins & Paper Money'), ('collectibles', 'Collectibles'), ('computers/tablets & networking', 'Computers/Tablets & Networking'), ('consumer electronics', 'Consumer Electronics'), ('crafts', 'Crafts'), ('dolls & bears', 'Dolls & Bears'), ('everything else', 'Everything Else'), ('gift cards & coupons', 'Gift Cards & Coupons'), ('health & beauty', 'Health & Beauty'), ('jewelry & watches', 'Jewelry & Watches'), ('music', 'Music'), ('musical instruments & gear', 'Musical Instruments & Gear'), ('pet supplies', 'Pet Supplies'), ('pottery & glass', 'Pottery & Glass'), ('sporting goods', 'Sporting Goods'), ('stamps', 'Stamps'), ('tickets & experiences', 'Tickets & Experiences'), ('toys & hobbies', 'Toys & Hobbies'), ('video games & consoles', 'Video Games & Consoles')], max_length=256, null=True),
        ),
        migrations.CreateModel(
            name='AuctionImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='auction_image')),
                ('auction_item_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authenticate.auctionitem')),
            ],
        ),
    ]