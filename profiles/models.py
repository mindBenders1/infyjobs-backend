from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User

from log.models import CompanyRegister
# Create your models here.

import datetime

year_dropdown = []
for y in range(1975, (datetime.datetime.now().year + 1)):
    year_dropdown.append((y, y))


class UserProfile(models.Model):
	user = models.OneToOneField(User)

	nationality = models.CharField(max_length=255)
	profile_pic = models.ImageField(upload_to='user_profile/profile_pic')
	contact_no = models.IntegerField()
	dob = models.DateField()
	school = models.CharField(max_length=255)
	tenth_cent = models.IntegerField()
	twelth_cent = models.IntegerField()
	college = models.CharField(max_length=255)
	course = models.CharField(max_length=255)
	cgpa = models.IntegerField()
	college_cent = models.IntegerField()
	more_courses = models.CharField(max_length=1024)
	bio = models.TextField()
	expertise = models.CharField(max_length=1024)
	skills = models.CharField(max_length=5000)
	website = models.URLField()
	resume = models.FileField(upload_to= 'userprofile/cv')
	created = models.DateTimeField(default=datetime.datetime.now)


	def __str__(self):
		return self.user.username


class AddExperience(models.Model):
	userprofile = models.OneToOneField(UserProfile)

	designation = models.CharField(max_length=255)
	company = models.CharField(max_length=255)
	worked_from = models.IntegerField(max_length=4, choices=year_dropdown)
	worked_to = models.IntegerField(max_length=4, choices=year_dropdown )

	def __str__(self):
		return self.userprofile.user.username + self.designation



class AddProject(models.Model):
	userprofile = models.OneToOneField(UserProfile)
	title = models.CharField(max_length=500)
	created_on = models.DateField()
	description = models.TextField()


	def __str__(self):
		return self.userprofile.user.username + self.title


#company
class AddMembers(models.Model):
	member = models.OneToOneField(User)
	company = models.OneToOneField(CompanyRegister)

	# name = models.CharField(max_length=1024)
	# email = models.EmailField()
	# password = models.CharField(max_length=20)
	contact_no = models.IntegerField()
	landline = models.IntegerField()
	designation = models.CharField(max_length=255)
	department = models.CharField(max_length=255)
	office_address = models.CharField(max_length=1024)
	city = models.CharField(max_length=255)
	state = models.CharField(max_length=255)
	country = models.CharField(max_length=255)
	profile_pic = models.ImageField(upload_to='company/members/profile_pic')


	def __str__(self):
		return self.company.company_name + self.name + self.department




