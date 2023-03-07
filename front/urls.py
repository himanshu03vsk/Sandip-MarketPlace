from django.urls import path
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from front import views

urlpatterns = [
    # Create
    path("buy_item", views.buy, name="buy"),
    path("sell", views.sell, name="sell"),
    path("auction", views.auction, name="auction"),
    path("post_ad", views.postad, name="posting_ad"),
    path("post_auction", views.postauction, name="post_auction"),
    path("add_payment", views.add_payment, name="add_payment"),
    # path("add_address", views.add_address, name="add_address"),



    # Read
    path("history", views.history, name="history"),
    path("ongoing_auctions", views.ongoing_auctions, name="ongoing_auctions"),
    path("payment_info", views.payment, name="payment_info"),
    path("buy_requests", views.buy_requests, name="buy_requests"),
    path("item/<int:item_id>", views.view_item  , name="view_item"),
    path("view_payment/<int:payment_id>", views.view_payment, name="view_payment"),
    
    # Update
    path("save_payment", views.save_payment, name="save_payment"),
    path("save_ad", views.save_address, name="save_address"),
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("success", views.success, name="success"),
    path("view_order/<int:order_id>", views.view_order, name="view_order"),

    
    # Ajax Paths #
    path("ajax/add_to_wishlist", views.add_to_wish, name="add_to_wish"),
    path("ajax/is_wishlisted", views.check_if_wish, name="is_wishlisted"),
    path("ajax/remove_from_wishlist", views.remove_from_wish, name="remove_from_wish"),
    path("ajax/update_fullfill", views.update_fulfillment, name="update_fullfillment"),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)