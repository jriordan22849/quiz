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
	
# get user selected answers
def completed(request):
	index = 1
	inner_index = 1
	number_answers = 0
	score = 0
	if request.method == "POST":	
		# get quiz name
		quiz_id = request.POST['name_of_quiz']
		quiz = Quiz.objects.get(quixID = quiz_id )
		print quiz
		# Get the number of questions for that quiz.
		numOfQuestions = request.POST['numOfqs']
		
		print("Quiz name : " + str(quiz_id))
		print("Num of Questions : " + str(numOfQuestions))
		
		# iterate throgh the numbe of questions
		while index <= int(numOfQuestions):
			ans  = request.POST.get(str(index), "No answer selected")		
			score += compareAnswer(quiz,index,ans)
			index = index + 1
		
	return render(request,'quiz/results.html', {'quiz':quiz, 'score':score, 'numOfQuestions':numOfQuestions})	


def compareAnswer(quiz, index, ans):
	score = 0
	
	print quiz
	
	questions = Question.objects.get(quizBelongTo=quiz, questionNumber = index)
	print questions
	
	option = Option.objects.get(option =questions, optionText = ans)
	print option
	
	if option.rightAnswer == False:
		score = 0
	else:
		score = score + 1

	
	return score