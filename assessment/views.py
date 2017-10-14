from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import AssessmentTest, Question
# Create your views here.


@login_required
def assessmentTestView(request):
	question_papers = AssessmentTest.objects.all()
	questions = Question.objects.all()

	return render(request, 'assessment/index.html', {'question_papers':question_papers, 'questions':questions})


