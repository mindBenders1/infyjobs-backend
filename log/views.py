from django.shortcuts import render
from .forms import UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from .models import CompanyRegister

def register(request):
	registered = False
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)

		if user_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()


			registered = True
			return HttpResponseRedirect(reverse('log:login'))
		else:
			print(user_form.errors, profile_form.errors)
	else:
		user_form = UserForm()
	return render(request, 'registration/user_register.html', {'registered':registered, 'user_form': user_form })


def user_login(request):
	if request.method == 'POST':
		username = request.POST.get("username")
		password = request.POST.get("password")

		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('log:dashboard'))
			else:
				return HttpResponse("Account is not active")
		else:
			print("someone tried to login with wrong credentials")

			return HttpResponse("invalid credentials")
	else:
		return render(request, 'registration/login.html', {})


@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('home:index'))














	# if request.method == 'POST':
	# 	user_form = UserForm(data=request.POST)

	# 	if user_form.is_valid():
	# 		user = user_form.save()
	# 		user.set_password(user.password)
	# 		user.save()

	# 		registered = True
	# 	else:
	# 		print(user_form.errors)
	# else:
	# 	user_form = UserForm()
	# return render(request, 'registration/user_register.html',{'registered':registered, 'user_form': user_form})


def company_register(request):
	if request.method == 'POST':
		company_name = request.POST['company_name']
		representative = request.POST['representative']
		website = request.POST['website']
		contact_no = request.POST['contact_no']
		office_address = request.POST['office_address']
		city = request.POST['city']
		state = request.POST['state']
		country = request.POST['country']
		CompanyRegister.objects.create(
			company_name=company_name, 
			representative=representative, 
			website=website, 
			contact_no=contact_no,
			office_address=office_address,
			city=city,
			state=state,
			country=country,
			)


	return HttpResponse('')




