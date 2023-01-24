from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager

# Create your models here.


class customer(AbstractUser):
    username = None
    email = models.EmailField(unique=True, primary_key=True, max_length=254)
    fname = models.CharField(max_length=200,null=True, blank=True)
    lname = models.CharField(max_length=200,null=True, blank=True)
    country = models.CharField(max_length=70,null=True, blank=True)
    institute = models.CharField(max_length=200,null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    last_login = models.DateTimeField(null=True, blank=True)



    object  = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    def __str__(self):
        return self.email
    

#unify this shit!
class auction_item(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=256)
    item_description = models.TextField()
    item_posted_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    is_sold = models.BooleanField(default=False, null=True, blank=True) # Obsolete and not necessary
    item_category = models.CharField(max_length=256,null=True, blank=True) #This can be converted to drop down of options field, 
    seller_id = models.ForeignKey(customer ,on_delete=models.CASCADE)

    # item_location = models.CharField(max_length=256,null=True)
    #Review the above line


class selling_item(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=256)
    item_description = models.TextField()
    item_posted_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    is_sold = models.BooleanField(default=False, null=True, blank=True)
    item_category = models.CharField(max_length=256,null=True, blank=True)
    seller_id = models.ForeignKey(customer ,on_delete=models.CASCADE)
    # item_location = models.CharField(max_length=256,null=True)
    #Review the above line

    def __str__(self) -> str:
        return self.item_name




class orders(models.Model):
    #Careful of the relationships and use on_delete wisely
    order_id = models.AutoField(primary_key=True)
    buyer_id = models.ForeignKey(customer, on_delete=models.CASCADE)
    item_for_sale = models.ForeignKey(selling_item,on_delete=models.CASCADE, blank=True, null=True)
    item_for_auction = models.ForeignKey(auction_item,on_delete=models.CASCADE, blank=True, null=True)
    order_status = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.item_for_sale

class auction(models.Model):
    auction_id = models.AutoField(primary_key=True)
    item = models.ForeignKey(auction_item, on_delete=models.CASCADE)
    posting_time = models.DateTimeField(auto_now=False, auto_now_add=True)
    is_sold = models.BooleanField(default=False, null=True, blank=True)
    final_bidder = models.ForeignKey(customer, related_name="buyer",on_delete=models.CASCADE, null=True, blank=True)
    seller_id = models.ForeignKey(customer,related_name="owner" , on_delete=models.CASCADE)
    auction_expiry = models.DateTimeField()
    highest_bid = models.CharField(max_length=256)  #The highest price for the auction item
    #no of bids = 
    #bids history 
    #TODO Not neccessary but if we have time, look into it
    


class bid(models.Model):
    bid_id = models.AutoField(primary_key=True)
    auction_id = models.ForeignKey(auction ,on_delete=models.CASCADE)
    bidder_id = models.ForeignKey(customer, on_delete=models.CASCADE, blank=True, null=True)
    bid_price = models.CharField(max_length=256, null=True, blank=True)
    status = None




class images(models.Model):
    item_id = models.ForeignKey(selling_item, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to="images/",
                              verbose_name='Image', null=True, blank=True)

    def __str__(self) -> str:
        return self.item_id.item_name