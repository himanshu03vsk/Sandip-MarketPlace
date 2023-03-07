from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from .models import Customer, Order, Payment, SellingItem, Auction, Bid, Image, Wishlist, Address


# # Register your models here.
# from .models import Account, selling_items, auction_items, orders

admin.site.register(SellingItem)
admin.site.register(Order)
# # admin.site.register(Account)
admin.site.register(Customer)
admin.site.register(Auction)
admin.site.register(Bid)
admin.site.register(Image)
admin.site.register(Wishlist)
admin.site.register(Address)
admin.site.register(Payment)




# class AccountAdmin(UserAdmin):
#     list_display = ('email', 'last_login', 'is_admin', 'is_staff')
#     list_display_links = ['email']
#     search_fields = ('email', 'username')
#     readonly_fields = ('data_joined', 'last_login')

#     filter_horizontal = ()
#     list_filter = ()
#     fieldsets = ()
# admin.site.register(Account, AccountAdmin)
