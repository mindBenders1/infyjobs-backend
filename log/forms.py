from django import forms
from django.contrib.auth.models import User

from .models import CompanyRegister
#from register.models import Userprofile

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta():
		model = User
		fields = ['first_name', 'last_name' ,'email', 'password']

class CompanyForm(forms.ModelForm):
	class Meta:
		model = CompanyRegister
		fields = '__all__'


