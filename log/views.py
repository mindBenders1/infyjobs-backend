from django.shortcuts import render
from .forms import UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import CompanyRegister
from jobs.models import CreateJob
from profiles.models import UserProfile

def index(request):
	return render(request, 'log/index.html', {})

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



@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('log:login'))

@login_required
def dashboard(request):
	if UserProfile.objects.filter(user=request.user).exists():
		user_profile = UserProfile.objects.get(user=request.user)
		profile_created = True
		marks = user_profile.marks
		if marks == 0:
			skill = user_register.skills
			eligible = CreateJob.objects.filter(skill_required=skill)
		else:
			eligible = CreateJob.objects.filter(marks_required__lte=marks)
			eligible = eligible.filter(skill_required=skill)
		return render(request, 'log/dashboard.html', {'profile_created': profile_created, 'eligible':eligible, 'marks':marks})
	else:
		profile_created = False
		return render(request, 'log/dashboard.html', {'profile_created': profile_created})

class CompanyRegisterView(CreateView):
	model = CompanyRegister
	fields = '__all__'











