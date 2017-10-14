from django.db import models
from datetime import datetime

# Create your models here.

class AssessmentTest(models.Model):
	subject = models.CharField(max_length=1024)
	date = models.DateTimeField(default=datetime.now)

	def __str__(self):
		return self.subject

class Question(models.Model):
	subject_details = models.ForeignKey(AssessmentTest)
	ques = models.TextField()
	opt1 = models.CharField(max_length=255)
	opt2 = models.CharField(max_length=255)
	opt3 = models.CharField(max_length=255)
	opt4 = models.CharField(max_length=255)
	ans = models.CharField(max_length=255)

	def __str__(self):
		return str(self.id)

