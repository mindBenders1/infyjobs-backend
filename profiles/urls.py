from django.conf.urls import url, include
from .views import  ShowProfile, CreateUserProfileView, add_member, EditProfileView

app_name='profiles'

urlpatterns = [
	# url(r'$', index, name='index'),
	url(r'^profile/$', ShowProfile, name='show_profile'),
	url(r'^create/$', CreateUserProfileView, name='create_profile'),
	url(r'^add_member/$', add_member, name='add_member'),
	url(r'^editprofile/(?P<pk>[0-9]+)/$', EditProfileView.as_view(), name='edit_profile'),
	
]


