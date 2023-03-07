from django.shortcuts import render, redirect
from .forms import Register
# from .forms import RegisterForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this



# Create your views here.
def user_dashboard(request):
	return render(request, "user_dashboard.html")

def user_login(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			print("valid")
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			# user = form.save()
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				print('done')
				messages.info(request,f'you are now logged in as {username}')
				return redirect("home")
		else:
			print("hh")
			messages.error(request, "Invalid credentials")
			messages.error(request, "invalid username")
	form = AuthenticationForm()
	return render(request, "user_login.html", context={"login_form": form})

def user_reg(request):
	if request.user.is_authenticated == True:
		print("user not auth")
		return render(request, "user_registration.html", {"access_denied": True})
	if request.method == "POST":
		# form = RegisterForm(request.POST)
		form = Register(request.POST)
		
		print(form.is_valid())

		print(form.errors)
		if form.is_valid():
			print("Valid")
			
			user = form.save()
			email = form.cleaned_data["email"]
			password = form.cleaned_data["password1"]
			# user = authenticate(username=username, password=password)
			# login(request, user, backend='django.contrib.auth.backends.ModelBackend') #comment this line if you dont want to immediately login after registration succeeds
			login(request, user) #comment this line if you dont want to immediately login after registration succeeds
			print("LOgin successfull")
			return redirect("home")
		return render(request, 'user_registration.html', {'form': form})
	else:
		form = Register()
		# form = RegisterForm()
	return render(request, "user_registration.html", {'form': form})
	# return render(request, "user_registration.html")


def logout_user(request):
	logout(request)
	return redirect("user_login")
