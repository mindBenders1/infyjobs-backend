from django.shortcuts import render
from .models import CreateJob
from .forms import CreateJobForm
# Create your views here.

def createJobView(request):
	if request.method == 'POST':
		job_title = request.POST['job_title']
		job_position = request.POST['job_position']
		job_qualification = request.POST['job_qualification']
		no_of_vacancy = request.POST['no_of_vacancy']
		job_description = request.POST['job_description']
		job_created = request.POST['job_created']
		job_last_date = request.POST['job_last_date']

		CreateJob.objects.create(
			job_title = job_title,
			job_position = job_position,
			job_qualification = job_qualification,
			no_of_vacancy = no_of_vacancy,
			job_description = job_description,
			job_created = job_created,
			job_last_date = job_last_date
			)
	return HttpResponse('')


def showJobs(request):
	jobs = CreateJob.objects.all()
	return HttpResponse('')