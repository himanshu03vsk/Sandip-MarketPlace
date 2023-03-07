from django import forms
from django.forms import ModelForm
from sys import path
path.append("..")
from authenticate.models import SellingItem, Image, Address, Payment, Customer
from datetime import date



#FORM TOPICS FOR SELLING

# Fashion: Eg Uniform, Watches etc
# Electronics: Heater, cooler, etc
# Furniture
# Academics: Assignments
# Misc
# Add general topics too(refer olx website)
# Event Passes
# Seperate categories based on academics and dormitories

#FORM TOPICS FOR Auction
# Collectibles,Antics
# Electronic
# Home decoration
# Post Permissions for doing business on college grounds
# Hand Made Items


# Student Utility
# Carpooling
# Events




class SellForm(ModelForm):
    class Meta:
        model = SellingItem
        fields = ['item_name','item_description','item_category', 'item_price']
        widgets = {'item_name':forms.TextInput(attrs={'class':'form-input'
                ,'required':''},), 
                 'item_description':forms.Textarea(attrs={'class':'form-input'
                ,'required':''}),

                'item_category':forms.TextInput(attrs={'class':'form-input', 'required':''}),

                'item_price':forms.TextInput(attrs={'class':'form-input', 'required':''})

            
            }

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'multiple': True}),
        }


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        exclude = ['user_id']
        


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        exclude = ['owner_id']
        widgets = {
            'expiry': forms.widgets.DateInput(attrs={'type': 'date', 'min': str(date.today())})
        }

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['fname', 'lname','country', 'institute','city']