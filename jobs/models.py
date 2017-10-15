from django.db import models
from profiles.models import AddMembers
from datetime import datetime
# Create your models here.
class CreateJob(models.Model):
	company_details = models.ForeignKey(AddMembers)

	job_title = models.CharField(max_length=255)
	job_position = models.CharField(max_length=255)
	job_qualification = models.CharField(max_length=255)
	no_of_vacancy = models.IntegerField()
	job_description = models.TextField()
	job_created_date = models.DateField(default=datetime.now)
	job_last_date = models.DateField()

	def _str__(self):
		return self.comapany_details.comapany.comapany_name + self.job_title