from django.shortcuts import render

# from .forms import NameForm
from .forms import SellForm, ImageForm
from sys import path

path.append("..")

from authenticate.models import SellingItem, Image
from django.shortcuts import render
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect




# Create your views here.
login_url = "/login"
@login_required(login_url=login_url)
def home(request):
    print(request.user)
    if request.user.is_authenticated:
        print("user is authenticated")
        name = request.user.email
        listings = SellingItem.objects.filter(is_sold=False)
        item_set = {}
        for i in listings:
            item_set[i.item_name] = [i, [j.image.url for j in i.image_set.all()]]
        return render(request, "index.html", {"name": name, "listings": item_set})
    return render(request, "index.html")


def buy(request):
    req_item = SellingItem.objects.get(pk=request.GET["item_id"])
    if req_item.is_sold:
        return render(request, "buy.html", {"sold": True})
    
    
    return render(request, "buy.html")

@login_required(login_url=login_url)
def sell(request):
    if request.method == "POST":
        form1 = SellForm(request.POST)
        form2 = ImageForm(request.POST, request.FILES)
        photos = request.FILES.getlist("image")
        if form1.is_valid() and form2.is_valid():
            fs = form1.save(commit=False)
            fs.seller_id = request.user
            fs.is_auction_item = False
            fs.item_location = request.user.institute
            fs.save()
            for image in photos:
                Image.objects.create(image=image, item_id=fs)
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

def view_item(request, item_id):
    item = SellingItem.objects.get(item_id=item_id)
    print(item.item_id)
    return render(request, "item.html", {"item":item, "images": item.image_set.all()})





def auction(request):
    #save the form if it is valid using fs.save(commit=False)
    #Then use the is_auction_item attribute to mark the item as auction item
    return render(request, "auction.html")


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
