from django.conf.urls import url, include
from .views import createJobView, showJobs, jobDetail

app_name = 'jobs'

urlpatterns = [
	url(r'^create/$', createJobView, name='create_job'),
	url(r'^show/$', showJobs, name='create_job'),
	url(r'^job/(?P<pk>[0-9]+)/$', jobDetail, name='job_detail'),
]	