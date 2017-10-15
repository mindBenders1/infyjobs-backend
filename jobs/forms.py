from django import forms
from .models import CreateJob

class CreateJobForm(forms.ModelForm):
	class Meta:
		model = CreateJob
		fields = '__all__'

