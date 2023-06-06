from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from .models import (
    Customer,
    Order,
    Payment,
    SellingItem,
    AuctionItem,
    Bid,
    Image,
    Wishlist,
    Address,
    AuctionImage,
    AuctionWishlist,
    Transaction
)


# # Register your models here.
# from .models import Account, selling_items, auction_items, orders

admin.site.register(SellingItem)
admin.site.register(Order)
# # admin.site.register(Account)
admin.site.register(Customer)
admin.site.register(AuctionItem)
admin.site.register(Bid)
admin.site.register(Image)
admin.site.register(AuctionImage)
admin.site.register(Wishlist)
admin.site.register(AuctionWishlist)
admin.site.register(Address)
admin.site.register(Payment)
admin.site.register(Transaction)



# class CustomerAdmin(admin.ModelAdmin):
#     list = ('email', 'fname', 'institute', 'last_login')
# admin.site.register(Customer, CustomerAdmin)

# class SellingItemAdmin(admin.ModelAdmin):
#     list = ('item_name', 'item_posted_at', 'is_sold', 'item_category', 'item_price')
#     # pass
# admin.site.register(SellingItem, SellingItemAdmin)
# class OrderAdmin(admin.ModelAdmin):
#     pass

# class AuctionAdmin(admin.ModelAdmin):
#     pass

# class ImageAdmin(admin.ModelAdmin):
#     pass


# class PaymentAdmin(admin.ModelAdmin):
#     pass


# class AccountAdmin(UserAdmin):
#     list_display = ('email', 'last_login', 'is_admin', 'is_staff')
#     list_display_links = ['email']
#     search_fields = ('email', 'username')
#     readonly_fields = ('data_joined', 'last_login')

#     filter_horizontal = ()
#     list_filter = ()
#     fieldsets = ()
# admin.site.register(Account, AccountAdmin)
