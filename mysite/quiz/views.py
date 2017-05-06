from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Quiz
from .models import Question
from .models import Option
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.

def viewqs(request):
	if request.user.is_authenticated():	
		quiz = Quiz.objects.all()
		print("Home Page")
		return render(request,'quiz/homepage.html', {'quiz':quiz})	
	else: 
		return render(request,'accounts/login.html', {'error':'To view a quiz, please login.'})
	

# retrieve the id of the quix picked by the user.
def picked(request, quixID):
	print(quixID)
	quiz = Quiz.objects.get(quixID=quixID)
	questions = Question.objects.filter(quizBelongTo=quiz)
	options = Option.objects.all()
	
	#print("Questions: " + str(questions))
	print("Options: " + str(options))
	return render(request,'quiz/quiz.html', {'quiz':quiz,'questions':questions,'options':options})	
	