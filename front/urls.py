from django.urls import path
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from front import views

urlpatterns = [
    path("", views.home, name="home"),
    path("buy_item", views.buy, name="buy"),
    path("sell", views.sell, name="sell"),
    path("auction", views.auction, name="auction"),
    path("about", views.about, name="about"),
    path("history", views.history, name="history"),
    path("ongoing_auctions", views.ongoing_auctions, name="ongoing_auctions"),
    path("payment", views.payment, name="payment"),
    path("post_ad", views.postad, name="posting_ad"),
    path("post_auction", views.postauction, name="post_auction"),
    path("item/<int:item_id>", views.view_item, name="view_item"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)