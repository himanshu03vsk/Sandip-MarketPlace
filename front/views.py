from django.shortcuts import render

# from .forms import NameForm
from .forms import SellForm, AuctionForm, ImageForm
from sys import path

path.append("..")

from authenticate.models import selling_item, auction_item, images
from django.shortcuts import render
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect




# Create your views here.
login_url = "/login"
# @login_required(login_url=login_url)
def home(request):
    print(request.user)
    if request.user.is_authenticated:
        print("user is authenticated")
        name = request.user.email
        listings = selling_item.objects.filter(is_sold=False)
        item_set = {}
        for i in listings:
            item_set[i.item_name] = [i, [j.image.url for j in i.images_set.all()]]
        return render(request, "index.html", {"name": name, "listings": item_set})
    return render(request, "index.html")


def buy(request):
    messages.add_message(request, messages.INFO, "Hello world.")
    return render(request, "buy.html")

@login_required
def sell(request):
    if request.method == "POST":
        form1 = SellForm(request.POST)
        form2 = ImageForm(request.POST, request.FILES)
        photos = request.FILES.getlist("image")
        if form1.is_valid() and form2.is_valid():
            fs = form1.save(commit=False)
            fs.seller_id = request.user
            fs.save()
            for image in photos:
                images.objects.create(image=image, item_id=fs)
            messages.success(request,"Successfully added image")
            return render(request,"sell.html")
        else:
            print("Error")
            print(form1.errors, form2.errors)
            return render(request,"sell.html")
    else:
        form1 = SellForm()
        form2 = ImageForm()
        return  render(request,"sell.html",{"form1":form1, "form2":form2})


def auction(request):
    if request.method == "POST":
        auction_form = AuctionForm(request.POST)
    else:
        auction_form = AuctionForm()
        return render(request, "auction.html", {"form": auction_form})


def about(request):
    return render(request, "about.html")


def history(request):
    return render(request, "history.html")


def ongoing_auctions(request):
    return render(request, "ongoing_auction.html")


def payment(request):
    return render(request, "payment.html")


def postad(request):
    return render(request, "posting_ad.html")


def postauction(request):
    return render(request, "posting_auction.html")
