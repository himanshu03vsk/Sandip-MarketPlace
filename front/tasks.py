from sys import path
path.append("..")
from django.utils import timezone
from authenticate.models import AuctionItem, Customer, Bid, Transaction
from celery import shared_task


@shared_task
def AuctionEndChecker():
    ended_auctions = AuctionItem.objects.filter(is_sold=False, end_time__lt=timezone.now())
    for item in ended_auctions:
        bid = Bid.objects.filter(auction_item_id=item.item_id).order_by('bid_price')[0]
        buyer = bid.bidder_id
        seller = item.seller_id
        amount = bid.bid_price
        Transaction.objects.create(buyer_id=buyer, seller_id=seller,item_id=item,transaction_amount=amount)
        item.is_sold = True
        item.save()









