from django import forms
from django.contrib.auth.models import User

from .models import UserProfile, AddExperience, AddProject, AddMembers
#from register.models import Userprofile


class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		exclude = ['user',]


class ExperienceForm(forms.ModelForm):
	class Meta:
		model = AddExperience
		fields = ['designation', 'company', 'worked_from', 'worked_to']



class ProjectForm(forms.ModelForm):
	class Meta:
		model = AddProject
		fields = ['title', 'created_on', 'description']


class MemberForm(forms.ModelForm):
	class Meta:
		model = AddMembers
		fields = '__all__'