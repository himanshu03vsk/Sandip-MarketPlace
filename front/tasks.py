from sys import path
path.append("..")
import datetime
from django.utils import timezone
from authenticate.models import AuctionItem, Customer, Bid, Transaction
from celery import shared_task


@shared_task(bind=True)
def AuctionEndChecker(self):
    print("Hiii")
    # auc = AuctionItem.objects.all()[0]
    # print("Item end time: ", auc.end_time, end=" ")
    # print("Current time: ", timezone.now(), end=" ")
    # print("Current time: ", datetime.datetime.now(), end=" ")

    ended_auctions = AuctionItem.objects.filter(is_sold=False, end_time__lt=datetime.datetime.now())
    print(ended_auctions)
    for item in ended_auctions:
        print(item, 'has to be ended')
        bid = Bid.objects.filter(auction_item_id=item.item_id).order_by('-bid_price')[0]
        # print([x.price for x in bid])
        buyer = bid.bidder_id
        seller = item.seller_id
        amount = bid.bid_price
        address = bid.bidder_id.address_set.all()[0]
        payment_mode = "Card"
        Transaction.objects.create(buyer_id=buyer, seller_id=seller,item_id=item,transaction_amount=amount, address=address, payment_mode=payment_mode)
        item.is_sold = True
        item.save()
        print(f'Executed {item.item_name} auction ending process')









