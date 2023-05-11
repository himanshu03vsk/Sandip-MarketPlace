from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager
from django.core.validators import MinLengthValidator

# Create your models here.
CHOICES = (('mumbai','Mumbai'), ('delhi','Delhi '), ('bengluru','Bengaluru'), ('hydrabad','Hyderabad '), ('ahmadabad','Ahmadabad'),
 ('chennai','Chennai '), ('kolkata','Kolkata '), ('surat','Surat '), ('pune','Pune '), ('jaipur','Jaipur '), ('lucknow','Lucknow ') ,('nashik','Nashik'),
( 'nagpur','Nagpur') ,('indore','Indore') ,('thane','Thane'))

class Customer(AbstractUser):

    first_name = None
    last_name = None
    username =  None
    email          = models.EmailField(unique=True, primary_key=True, max_length=254)
    fname          = models.CharField(max_length=200,null=True, blank=True)
    lname          = models.CharField(max_length=200,null=True, blank=True)
    country        = models.CharField(max_length=70,null=True, blank=True)
    institute      = models.CharField(max_length=200,null=True, blank=True)
    city           = models.CharField(max_length=50, choices=CHOICES, default='mumbai', null=True, blank=True)
    last_login     = models.DateTimeField(null=True, blank=True)
    object  = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    


category_choices = (
("Art".lower(),"Art"),
("antiques","Antiques"),
("Books & Magazines".lower(),
"Books & Magazines"),
("Cameras & Photo".lower(), "Cameras & Photo"),
("Cell Phones & Accessories".lower(), "Cell Phones & Accessories"),
("Clothing, Shoes & Accessories".lower(), "Clothing, Shoes & Accessories"),
("Coins & Paper Money".lower(), "Coins & Paper Money"),
("Collectibles".lower(), "Collectibles"),
("Computers/Tablets & Networking".lower(), "Computers/Tablets & Networking"),
("Consumer Electronics".lower(), "Consumer Electronics"),
("Crafts".lower(), "Crafts"),
("Dolls & Bears".lower(), "Dolls & Bears"),
("Everything Else".lower(), "Everything Else"),
("Gift Cards & Coupons".lower(), "Gift Cards & Coupons"),
("Health & Beauty".lower(), "Health & Beauty"),
("Jewelry & Watches".lower(), "Jewelry & Watches"),
("Music".lower(), "Music"),
("Musical Instruments & Gear".lower(), "Musical Instruments & Gear"),
("Pet Supplies".lower(), "Pet Supplies"),
("Pottery & Glass".lower(), "Pottery & Glass"),
("Sporting Goods".lower(), "Sporting Goods"),
("Stamps".lower(), "Stamps"),
("Tickets & Experiences".lower(), "Tickets & Experiences"),
("Toys & Hobbies".lower(), "Toys & Hobbies"),
("Video Games & Consoles".lower(), "Video Games & Consoles"),

)
#unify this shit!
class AuctionItem(models.Model):

    item_id                 = models.AutoField(primary_key=True)
    item_name               = models.CharField(max_length=256)
    item_description        = models.TextField()
    start_time              = models.DateTimeField(null=True, blank=True)
    end_time                = models.DateTimeField(null=True, blank=True)       #
    posted_at               = models.DateTimeField(auto_now_add=True ,null=True,blank=True)
    starting_price          = models.FloatField(default=100.0, blank=True, null=True) 
    current_bid             = models.FloatField(blank=True, null=True)
    seller_id               = models.ForeignKey(Customer ,on_delete=models.CASCADE)
    is_sold                 = models.BooleanField(default=False, null=True, blank=True)
    item_category           = models.CharField(max_length=256, choices=category_choices, null=True, blank=True)
    item_location           = models.TextField(null=True, blank=True)
    
    #Review the above line

    def __str__(self):
        return self.item_name
class SellingItem(models.Model):
    item_id             = models.AutoField(primary_key=True)
    item_name           = models.CharField(max_length=256)
    item_description    = models.TextField()
    item_posted_at      = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    is_sold             = models.BooleanField(default=False, null=True, blank=True)
    item_category       = models.CharField(max_length=256, choices=category_choices,null=True, blank=True)
    seller_id           = models.ForeignKey(Customer ,on_delete=models.CASCADE)
    item_location       = models.TextField(null=True, blank=True)
    item_price          = models.FloatField(null=True, blank=True)
    #Review the above line

    def __str__(self) -> str:
        return self.item_name




class Order(models.Model):
    #Careful of the relationships and use on_delete wisely
    order_id            = models.AutoField(primary_key=True)
    seller_id           = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="seller_id_for_order", blank=True, null=True)
    buyer_id            = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    item_for_sale       = models.ForeignKey(SellingItem,on_delete=models.CASCADE, blank=True, null=True)
    # item_for_Auction    = models.ForeignKey(Auction_item,on_delete=models.CASCADE, blank=True, null=True)
    is_dispatched       = models.BooleanField(default=False, null=True, blank=True)
    order_status        = models.BooleanField(default=False, null=True, blank=True)
    address             = models.TextField(default="some building")                 
    payment_method      = models.TextField(default="some payment")
    card_info           = models.TextField(default="some card info")
    price               = models.TextField(default="100", null=True, blank=True)
    created_at          = models.DateTimeField(auto_now_add=True ,null=True, blank=True)

    def __str__(self):
        return self.item_for_sale.item_name

# class Auction(models.Model):
#     Auction_id          = models.AutoField(primary_key=True)
#     item                = models.ForeignKey(SellingItem, on_delete=models.CASCADE)
#     posting_time        = models.DateTimeField(auto_now=False, auto_now_add=True)
#     is_sold             = models.BooleanField(default=False, null=True, blank=True)
#     final_bidder        = models.ForeignKey(Customer, related_name="buyer",on_delete=models.CASCADE, null=True, blank=True)
#     seller_id           = models.ForeignKey(Customer,related_name="owner" , on_delete=models.CASCADE)
#     Auction_expiry      = models.DateTimeField()
#     highest_bid         = models.CharField(max_length=256)  #The highest price for the Auction item
#     #no of bids = 
#     #bids history 
#     #TODO Not neccessary but if we have time, look into it
    
class Transaction(models.Model):
    transaction_id          = models.AutoField(primary_key=True)
    buyer_id                = models.ForeignKey(Customer, related_name="buyer_id_for_transaction", on_delete=models.CASCADE)
    seller_id               = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="seller_id_for_transaction")
    item_id                 = models.ForeignKey(AuctionItem, on_delete=models.CASCADE)
    transaction_time        = models.DateTimeField(auto_now_add=True)
    transaction_amount      = models.FloatField()

class Bid(models.Model):
    bid_id                  = models.AutoField(primary_key=True)
    auction_item_id         = models.ForeignKey(AuctionItem ,on_delete=models.CASCADE, null=True, blank=True)
    bidder_id               = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    bid_price               = models.FloatField()
    bid_time                = models.DateTimeField(auto_now_add=True)
    status                  = None

    def __str__(self):
        return f"{self.bid_price} by {self.bidder_id.fname} for {self.auction_item_id.item_name}"



class Image(models.Model):
    item_id             = models.ForeignKey(SellingItem, on_delete=models.CASCADE, blank=True, null=True)
    image               = models.ImageField(upload_to="images/",verbose_name='Image', null=True, blank=True)

    def __str__(self) -> str:
        return self.item_id.item_name


class AuctionImage(models.Model):
    auction_item_id = models.ForeignKey(AuctionItem, on_delete=models.CASCADE, blank=True, null=True)
    image           = models.ImageField(upload_to='images/', verbose_name="auction_image", null=True, blank=True)
    

    def __str__(self):
        return self.auction_item_id.item_name

class Address(models.Model):
    user_id             = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    
    phone               = models.CharField(max_length=20)
    address1            = models.CharField(max_length=50)
    address2            = models.CharField(max_length=200)
    address3            = models.CharField(max_length=120)
    city                = models.CharField(max_length=120)
    state               = models.CharField(max_length=100)
    country             = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.user_id.email + "'s Address"

    
class Wishlist(models.Model):
    wishlist_owner_id               = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    item_id                         = models.ForeignKey(SellingItem, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return self.item_id.item_name + "wished by "

class AuctionWishlist(models.Model):
    owner_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    auction_item_id = models.ForeignKey(AuctionItem, on_delete=models.CASCADE)

    def __str__(self):
        return self.auction_item_id.item_name


class Payment(models.Model):
    payment_id                      = models.AutoField(primary_key=True)
    owner_id                        = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    card_holder_name                = models.TextField(null=True)
    card_number                     = models.TextField(null=True, max_length=16,validators=[MinLengthValidator(16, 'The Card number must have 16 digits')])
    expiry                          = models.DateField(null=True)

    def __str__(self) -> str:
        return self.owner_id.email + " card ending with " + self.card_number[-4:]
    
