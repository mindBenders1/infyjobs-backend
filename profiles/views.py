from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from .models import UserProfile, AddMembers

# Create your views here.
# def index(request):
# 	pass
@login_required
def ShowProfile(request):
	user_profile = UserProfile.objects.get(user=request.user)
	return render(request, 'profiles/profile.html', {'user_profile':user_profile})


class CreateUserProfileView(CreateView):
	model = UserProfile
	




# @login_required
# def CreateUserProfileView(request):
# 	if request.method == 'POST':
# 		user = request.user
# 		nationality = request.POST['nationality']
# 		profile_pic = request.POST['profile_pic']
# 		contact_no = request.POST['contact_no']
# 		dob = request.POST['dob']
# 		school = request.POST['school']
# 		tenth_cent = request.POST['tenth_cent']
# 		twelth_cent = request.POST['twelth_cent']
# 		college = request.POST['college']
# 		course = request.POST['course']
# 		cgpa = request.POST['cgpa']
# 		college_cent = request.POST['college_cent']
# 		more_courses = request.POST['more_courses']
# 		bio = request.POST['bio']
# 		expertise = request.POST['expertise']
# 		skills = request.POST['skills']
# 		website = request.POST['website']
# 		resume = request.FILES['resume']
# 		created = request.POST['created']

# 		UserProfile.objects.create(
# 			user = user,
# 			nationality = nationality,
# 			profile_pic = profile_pic,
# 			contact_no = contact_no,
# 			dob = dob,
# 			school = school,
# 			tenth_cent = tenth_cent,
# 			twelth_cent = twelth_cent,
# 			college = college,
# 			course = course,
# 			cgpa = cgpa,
# 			college_cent = college_cent,
# 			more_courses = more_courses,
# 			bio = bio,
# 			expertise = expertise,
# 			skills = skills,
# 			website = website,
# 			resume = resume,
# 			created = created
# 			)

# 	return HttpResponse('')


def add_member(request):
	return HttpResponse('')