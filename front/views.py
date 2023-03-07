from django.shortcuts import render
# from .forms import NameForm
from .forms import SellForm, ImageForm, AddressForm, PaymentForm, CustomerForm
from sys import path

path.append("..")
from django.urls import reverse
from authenticate.models import SellingItem, Order, Image, Address, Wishlist,Customer, Payment
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
    print(request.GET.get('institute',''))
    unis = Customer.objects.values('institute').distinct()
    unis_names = [i['institute'] for i in unis]
    if request.user.is_authenticated:
        if bool(request.GET.get('institute','')):
            listings = SellingItem.objects.filter(is_sold=False,item_location=request.GET['institute']).exclude(seller_id=request.user)
        else:
            listings = SellingItem.objects.filter(is_sold=False).exclude(seller_id=request.user)
        name = request.user.email
        item_set = {}
        for i in listings:
            item_set[i.item_name] = [i, [j.image.url for j in i.image_set.all()]]
        return render(request, "index.html", {"name": name, "listings": item_set, 'unis': unis_names, 'selected_uni': request.GET.get('institute','')})
    return render(request, "index.html", {'unis': unis_names, 'selected_uni': request.GET.get('institute','')})




@login_required(login_url=login_url)
def buy(request):
    req_item = SellingItem.objects.get(pk=request.GET["item_id"])
    seller = req_item.seller_id
    if request.user == seller:
        print(True)
        return render(request, "buy.html", {"same_user": True})

    if req_item.is_sold:
        return render(request, "buy.html", {"sold": True})
    
    addresses = Address.objects.filter(user_id=request.user)
    payment = Payment.objects.filter(owner_id=request.user)
    payment_form = None
    if bool(payment) == False:
        no_payment = True
        payment_form = PaymentForm()
    else:
        no_payment = False

    no_address = None
    if bool(addresses)== False:

        # print(" ia m here")
        form = AddressForm()
        no_address = True
        return render(request, "buy.html", {"form": form, "address_flag": no_address})
     
    


    return render(request, "buy.html", {"addresses": addresses, "no_payment":no_payment, "payment_form": payment_form, "payment": payment})

@login_required(login_url=login_url)
def success(request):
    print(request.POST)
    data = {}
    data["buyer_id"] = Customer.object.get(email=request.POST["buyer_id"])
    item_id = request.POST["item_id"]
    data["address"] = request.POST["address"]
    data["payment_method"] = request.POST["payment_method"]
    data["item_for_sale"] = SellingItem.objects.get(item_id=item_id)
    if data["item_for_sale"].is_sold:
        reason = "Item is already sold"
        print("I am here")
        return render(request, "failed.html",{"reason":reason})
    data["seller_id"] = data["item_for_sale"].seller_id
    card_flag = False if data["payment_method"].lower() == "cod"  else True
    
    data["price"] = data["item_for_sale"].item_price
    if card_flag:
        data["card_info"] = request.POST["card_info"]
    print(data)
    # return HttpResponseRedirect("/")
    a = Order.objects.create(**data)
    temp = SellingItem.objects.get(item_id=item_id)
    temp.is_sold = True
    temp.save()
    return render(request, "success.html")

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
    trans_desc = {}
    raw_desc = item.item_description.split(";")
    for i in raw_desc:
        cat = i.split(":")
        trans_desc[cat[0]] = cat[1]
    return render(request, "item.html", {"item":item, "images": item.image_set.all(), "item_description": trans_desc.items()})

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

@login_required(login_url=login_url)
def add_payment(request):
    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            print("form is valid")
            f = form.save(commit=False)
            f.owner_id = request.user
            f.save()
            return HttpResponseRedirect("/payment_info")
    form = PaymentForm()
    print("I am here")
    return render(request, "add_payment.html", {"form": form})

def save_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        f = form.save(commit=False)
        f.owner_id = request.user
        next = request.POST.get('next', '/')
        if form.is_valid():
            f.save()
            return HttpResponseRedirect(next)
        else:
            messages.error(request, "There was an error saving")
            return render(request, "buy.html")





def check_if_wish(request):
    item_id = request.GET.get('item_id', None)
    user = request.GET.get('user', None)
    data = {}
    if Wishlist.objects.filter(wishlist_owner_id=user, item_id=item_id).exists():
        data["exists"] = True
        return JsonResponse(data)
    data["exists"] = False
    # print("item not there")
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




def buy_requests(request):
    items = Order.objects.filter(seller_id=request.user, order_status=False)
    print(items)
    return render(request, "requests.html", {"items": items})

def auction(request):
    #save the form if it is valid using fs.save(commit=False)
    #Then use the is_auction_item attribute to mark the item as auction item
    return render(request, "auction.html")


def about(request):
    if request.method == "POST":
        profile_info = CustomerForm(request.POST, instance=request.user)
        profile_info.save()
        # profile_form = CustomerForm(instance=profile_info)
        return render(request, "about.html",  {"profile_form":profile_info})
    profile_info = Customer.objects.get(email=request.user)
    print(profile_info.institute)
    #  = CustomerForm()
    profile_form = CustomerForm(instance=profile_info)
    return render(request, "about.html", {"profile_form":profile_form})


def history(request):
    items = Order.objects.filter(buyer_id=request.user)
    print(items)
    return render(request, "history.html", {"items": items})

@login_required(login_url=login_url)
def view_order(request, order_id):
    # print(order)
    req_order = Order.objects.get(order_id=order_id)
    print(req_order)
    return render(request, "order.html", {"i": req_order})

@login_required(login_url=login_url)
def update_fulfillment(request):
    print("HI")
    data = {}
    order_id = request.GET.get('order_id', None)
    order = Order.objects.get(order_id=order_id)
    order.order_status = True
    order.save()
    data["success"] = True
    print("done")
    print(data)
    return JsonResponse(data)


def ongoing_auctions(request):
    return render(request, "ongoing_auction.html")



def payment(request):
    payment_infos = Payment.objects.filter(owner_id=request.user)
    # print(payment_infos[0].card_number)
    return render(request, "payment.html", {"payment_forms": payment_infos})

@login_required(login_url=login_url)
def view_payment(request, payment_id):
    if request.method=="POST":
        item = Payment.objects.get(payment_id=payment_id)
        form = PaymentForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/payment_info')
        # return render(request, "view_payment.html", {"form":form})
    item = Payment.objects.get(payment_id=payment_id)
    form = PaymentForm(instance=item)
    return render(request, "view_payment.html", {"form":form})

def postad(request):
    return render(request, "posting_ad.html")


def postauction(request):
    return render(request, "posting_auction.html")
