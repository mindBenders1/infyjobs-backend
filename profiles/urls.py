from django.conf.urls import url, include
from .views import index
from profiles.api import views as api_views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
	url(r'^$', index, name='index'),
	url(r'^api/profiles/', api_views.UserProfileListCreateAPIView.as_view(), name='api_all_profiles'),
	url(r'^api/profile/(?P<pk>[0-9]+)$', api_views.UserProfileRetrieveUpdateDestroyAPIView.as_view(), name='api_profile'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
