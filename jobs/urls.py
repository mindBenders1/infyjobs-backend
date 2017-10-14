from django.conf.urls import url, include
from .views import createJobView

app_name = 'jobs'

urlpatterns = [
	url(r'^jobs/create/$', createJobView, name='create_job'),
]	