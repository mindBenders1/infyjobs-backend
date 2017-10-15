from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import AssessmentTest, Question
from profiles.models import UserProfile 
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

# Create your views here.


@login_required
def assessmentTestView(request):
	question_papers = AssessmentTest.objects.all()
	questions = Question.objects.all()

	return render(request, 'assessment/index.html', {'question_papers':question_papers, 'questions':questions})


@login_required
def get_marks(request):
	if request.method == 'POST':
		user_profile = UserProfile.objects.get(user=request.user)
		user_profile.marks = request.POST['marks']
		user_profile.save()
		return HttpResponseRedirect(reverse('log:dashboard'))


