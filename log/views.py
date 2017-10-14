from django.shortcuts import render
from .forms import UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

# Create your views here.

def register(request):
	registered = False
	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		password = request.POST['password']
		user = User(first_name=first_name, last_name=last_name, email=email, password=password)
		user.set_password(password)

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
