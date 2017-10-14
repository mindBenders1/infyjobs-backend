from django import forms
from django.contrib.auth.models import User

from .models import CompanyRegister
#from register.models import Userprofile

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta():
		model = User
<<<<<<< HEAD
		fields = ['first_name', 'last_name','username' ,'email', 'password']
=======
		fields = ['first_name', 'last_name' ,'email', 'password']
>>>>>>> 0120d75396f3d44a94c5bb244fe998982b2ff3ff

class CompanyForm(forms.ModelForm):
	class Meta:
		model = CompanyRegister
		fields = '__all__'


