from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class CompanyRegister(models.Model):
	company_name = models.CharField(max_length=255)
	representative = models.CharField(max_length=255)
	website = models.URLField()
	contact_no = models.IntegerField()
	office_address = models.CharField(max_length=1024)
	city = models.CharField(max_length=255)
	state = models.CharField(max_length=255)
	country = models.CharField(max_length=255)



	def __str__(self):
		return self.company_name + self.representative

