from django.shortcuts import render
from .forms import UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from .models import CompanyRegister
# Create your views here.

def register(request):
	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		password = request.POST['password']
		user = User(first_name=first_name, last_name=last_name, email=email, password=password)
		user.set_password(password)
		user.save()

	return HttpResponse('')


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




