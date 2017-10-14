from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

app_name = 'log'

urlpatterns = [
	url(r'^login/$', login, name='login'),
	url(r'^logout/$', views.user_logout, name='logout'),
	url(r'^register/$', views.register, name='register'),
	url(r'^dashboard/$', views.dashboard, name='dashboard'),
	url(r'^company-register/$', views.CompanyRegisterView.as_view(), name='company_register'),
	
]