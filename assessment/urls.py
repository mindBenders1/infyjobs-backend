from django.conf.urls import url
from .views import assessmentTestView, get_marks

urlpatterns = [
	url(r'^test/$', assessmentTestView, name='assessmentTestView'),
	url(r'^get_marks/$', get_marks, name='get_marks'),
]