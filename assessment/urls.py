from django.conf.urls import url
from .views import assessmentTestView

urlpatterns = [
	url(r'test/$', assessmentTestView, name='assessmentTestView')
]