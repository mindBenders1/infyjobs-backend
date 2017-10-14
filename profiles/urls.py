from django.conf.urls import url, include
from .views import  ShowProfile


urlpatterns = [
	# url(r'$', index, name='index'),
	url(r'profile/$', ShowProfile, name='show_profile')
	
]


