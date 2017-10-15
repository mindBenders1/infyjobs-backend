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
	marks_required = models.IntegerField()
	skill_required = models.CharField(max_length=100)

	def __str__(self):
		return self.company_details.company.company_name + '-' +self.job_title