from django.shortcuts import render
from django.core.urlresolvers import reverse
from .models import CreateJob
from .forms import CreateJobForm
# Create your views here.


def createJobView(request):
	if request.method == 'POST':
		job_form = CreateJobForm(data=request.POST)

		if job_form.is_valid():
			job = job_form.save()
			return render(request, 'log/index.html', {})

	else:
		job_form = CreateJobForm()

	return render(request, 'jobs/createjob_form.html', {'job_form': job_form})

def showJobs(request):
	jobs = CreateJob.objects.all()
	return render(request, 'jobs/show.html', {'jobs':jobs})


def jobDetail(request,pk):
	job = CreateJob.objects.get(pk=pk)
	return render(request, 'jobs/job_detail.html', {'job':job})