from django import forms
from .models import CreateJob

class CreateJobForm(forms.ModelForm):
	model = CreateJob

