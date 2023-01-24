from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from .models import customer, orders, selling_item, auction_item, auction, bid, images


# # Register your models here.
# from .models import Account, selling_items, auction_items, orders

admin.site.register(selling_item)
admin.site.register(auction_item)
admin.site.register(orders)
# # admin.site.register(Account)
admin.site.register(customer)
admin.site.register(auction)
admin.site.register(bid)
admin.site.register(images)




# class AccountAdmin(UserAdmin):
#     list_display = ('email', 'last_login', 'is_admin', 'is_staff')
#     list_display_links = ['email']
#     search_fields = ('email', 'username')
#     readonly_fields = ('data_joined', 'last_login')

#     filter_horizontal = ()
#     list_filter = ()
#     fieldsets = ()
# admin.site.register(Account, AccountAdmin)
