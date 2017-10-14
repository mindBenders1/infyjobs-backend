from django.shortcuts import render
from .forms import UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import CompanyRegister

def index(request):
	return render(request, './index.html', {})

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


# def user_login(request):
# 	if request.method == 'POST':
# 		username = request.POST.get("username")
# 		password = request.POST.get("password")

# 		user = authenticate(username=username, password=password)

# 		if user:
# 			if user.is_active:
# 				login(request, user)
# 				return HttpResponseRedirect(reverse('log:dashboard'))
# 			else:
# 				return HttpResponse("Account is not active")
# 		else:
# 			print("someone tried to login with wrong credentials")

# 			return HttpResponse("invalid credentials")
# 	else:
# 		return render(request, 'registration/login.html', {})


@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('log:login'))

@login_required
def dashboard(request):
	return render(request, 'log/dashboard.html', {})

class CompanyRegisterView(CreateView):
	model = CompanyRegister
	fields = '__all__'











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






