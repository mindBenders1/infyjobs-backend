from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import UserProfile
from .forms import UserProfileForm, MemberForm, ExperienceForm, ProjectForm

# Create your views here.
# def index(request):
# 	pass
@login_required
def ShowProfile(request):
	user_profile = UserProfile.objects.get(user=request.user)
	return render(request, 'profiles/profile.html', {'user_profile':user_profile})

@login_required
def CreateUserProfileView(request):
	if request.method == 'POST':
		profile_form = UserProfileForm(data=request.POST)
		experience_form = ExperienceForm(data=request.POST)
		project_form = ProjectForm(data=request.POST)


		if profile_form.is_valid() and experience_form.is_valid() and project_form:

			profile = profile_form.save(commit=False)
			profile.user = user

			if 'profile_pic' in request.FILES:
				profile.profile_pic = request.FILES['profile_pic']

			if 'resume' in request.FILES:
				profile.resume = request.Files['resume']

			profile.save()


			experience = experience_form.save()
			project = profile_form.save()
	else:
		profile_form = UserProfileForm()
		experience_form = ExperienceForm()
		project_form = ProjectForm()
	return render(request, 'profiles/userprofile.html', {'profile_form':profile_form, 'experience_form':experience_form, 'project_form':project_form})



def add_member(request):
	if request.method == 'POST':
		member_form = MemberForm(data=request.POST)

		if member_form.is_valid():
			member = member_form.save(commit=False)
			password = request.POST['password']
			member.set_password(password)
			if 'profile_pic' in request.FILES:
				member.profile_pic = request.FILES['profile_pic']
			member.save()

	else:
		member_form = MemberForm()

	return render(request, 'profiles/member_form.html', {'member_form':member_form})

class EditProfileView(UpdateView):
	model = UserProfile
	fields = ['nationality','profile_pic','contact_no','dob','school','tenth_cent','twelth_cent','college','course','cgpa','college_cent','more_courses','bio','expertise','skills','website','resume','created']