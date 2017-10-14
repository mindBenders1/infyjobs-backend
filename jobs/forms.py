from django import forms
from .models import CreateJob

class CreateJobForm(forms.ModelForm):
	model = CreateJob
	fields = exclude('company_details')

