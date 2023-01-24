from django import forms
from django.forms import ModelForm
from sys import path
path.append("..")
from authenticate.models import selling_item, auction_item, images




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
        model = selling_item
        fields = ['item_name','item_description','item_category']
        widgets = {'item_name':forms.TextInput(attrs={'class':'form-input'
                ,'required':''},), 
                 'item_description':forms.Textarea(attrs={'class':'form-input'
                ,'required':''}),

                'item_category':forms.TextInput(attrs={'class':'form-input'})
            
            }

class ImageForm(forms.ModelForm):
    class Meta:
        model = images
        fields = ['image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'multiple': True}),
        }

class AuctionForm(ModelForm):
    class Meta:
        model = auction_item
        fields = ["item_name","item_description","item_category"]


