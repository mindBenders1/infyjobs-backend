from django.shortcuts import render
from .models import CreateJob
from .forms import CreateJobForm
# Create your views here.

def createJobView(request):
	

def showJobs(request):
	jobs = CreateJob.objects.all()
	return HttpResponse('')