from django.conf.urls import url, include
from .views import  ShowProfile, CreateUserProfileView

app_name='profiles'

urlpatterns = [
	# url(r'$', index, name='index'),
	url(r'^profile/$', ShowProfile, name='show_profile'),
	url(r'^create/$', CreateUserProfileView, name='create_profile'),
	# url(r'^editprofile/(?P<pk>[0-9]+)/$', CreateUserProfileView, name='edit_profile'),
	
]


