from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from .models import Account, Users
from .models import customer


class Register(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'form-input',
        'required':'',
        'name':'email',
        'id':'email',
        'type':'text',
        'placeholder':'JohnDoe12@mail.com',
        'maxlength':'50',
        'minlength':'6'

    }),max_length=255),

    fname = forms.CharField(label="First Name",widget=forms.TextInput(attrs={
        'class': 'form-input',
        'required':'',
        'name':'fname',
        'id':'fname',
        'type':'text',
        'placeholder':'John',
        'maxlength':'50',
        'minlength':'6'

    }),max_length=255)


    lname = forms.CharField(label="Last Name",widget=forms.TextInput(attrs={
        'class': 'form-input',
        'required':'',
        'name':'lname',
        'id':'lname',   
        'type':'text',
        'placeholder':'Doe',
        'maxlength':'50',
        'minlength':'6'
    }),max_length=255)
    
    
    city = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-input',
        'required':'',
        'name':'city',
        'id':'city',
        'type':'text',
        'placeholder':'Mumbai',
        'maxlength':'50',
        'minlength':'6'

    }),max_length=255)

    country = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-input',
        'required':'',
        'name':'location',
        'id':'location',
        'type':'text',
        'placeholder':'India',
        'maxlength':'50',
        'minlength':'6'

    }),max_length=255)

    institute = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-input',
        'required':'',
        'name':'institute',
        'id':'institute',
        'type':'text',
        'placeholder':'Sandip University',
        'maxlength':'200',
        'minlength':'6'

    }),max_length=255)


    class Meta:
        model = customer
        fields = ('email', 'fname', 'lname', 'city', 'country', 'institute', )
        # labels = {'user_id': 'Enter User ID','fname':'First Name', 'lname':'Last Name', 'password':'Password', 'email':'Email', 'city':'City', 'country':'Country', 'institute':'Institute Name'}
    
