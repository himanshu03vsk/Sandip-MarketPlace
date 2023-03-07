from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from .models import Account, Users
from .models import Customer
CHOICES = (('mumbai','Mumbai'), ('delhi','Delhi '), ('bengluru','Bengaluru'), ('hydrabad','Hyderabad '), ('ahmadabad','Ahmadabad'),
 ('chennai','Chennai '), ('kolkata','Kolkata '), ('surat','Surat '), ('pune','Pune '), ('jaipur','Jaipur '), ('lucknow','Lucknow ') ,('nashik','Nashik'),
( 'nagpur','Nagpur') ,('indore','Indore') ,('thane','Thane'))

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
    
    
    city = forms.ChoiceField(choices=CHOICES,widget=forms.Select(attrs={
        'class': 'form-input',

    }))

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
        model = Customer
        fields = ('email', 'fname', 'lname', 'city', 'country', 'institute', )
        # labels = {'user_id': 'Enter User ID','fname':'First Name', 'lname':'Last Name', 'password':'Password', 'email':'Email', 'city':'City', 'country':'Country', 'institute':'Institute Name'}
    
