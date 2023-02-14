from django.shortcuts import render
# from .forms import NameForm
from .forms import SellForm, ImageForm, AddressForm
from sys import path

path.append("..")
from django.urls import reverse
from authenticate.models import SellingItem, Image, Address, Wishlist,Customer
from django.shortcuts import render
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse




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

@login_required(login_url=login_url)
def buy(request):
    req_item = SellingItem.objects.get(pk=request.GET["item_id"])

    if req_item.is_sold:
        return render(request, "buy.html", {"sold": True})
    
    addresses = Address.objects.filter(user_id=request.user)


    no_address = None
    if bool(addresses)== False:
        # print(" ia m here")
        form = AddressForm()
        no_address = True
        return render(request, "buy.html", {"form": form, "address_flag": no_address})
     
    return render(request, "buy.html", {"addresses": addresses})


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

@login_required(login_url=login_url)
def save_address(request):
    if request.method == "POST":
        print(request.POST)
        # break
        form = AddressForm(data=request.POST)
        print(form.is_valid())
        f = form.save(commit=False)
        f.user_id = request.user
        next = request.POST.get('next', '/')
        if form.is_valid():
            f.save()
            print("redirected")
            return HttpResponseRedirect(next)
        else:
            # print(form.errors)
            messages.error(request, "There was an error in saving the address, please try again")
            return render(request, "buy.html")

def add_to_wish(request):
    print("request send")
    item_id = request.GET.get('item_id', None)
    user = request.GET.get('user', None)
    item = SellingItem.objects.get(item_id=item_id)
    data = {}
    # if Wishlist.objects.filter(wishlist_owner_id=user, item_id=item_id).exists():
    #     data["exists"] = True
    #     return JsonResponse(data)
    wish_entry = Wishlist.objects.create(wishlist_owner_id=request.user, item_id=SellingItem.objects.get(item_id=item_id))
    wish_entry.save()
    data["success"] = True
    return JsonResponse(data)




def check_if_wish(request):
    item_id = request.GET.get('item_id', None)
    user = request.GET.get('user', None)
    data = {}
    if Wishlist.objects.filter(wishlist_owner_id=user, item_id=item_id).exists():
        data["exists"] = True
        return JsonResponse(data)
    data["exists"] = False
    print("item not there")
    return JsonResponse(data)





def remove_from_wish(request):
    item_id = request.GET.get('item_id', None)
    user = request.GET.get('user', None)
    data = {}
    Wishlist.objects.filter(wishlist_owner_id=user, item_id=item_id).delete()
    data["exists"] = False
    print("removed")
    messages.success(request, "Successfully removed the item from the wishlist")
    return JsonResponse(data)

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
