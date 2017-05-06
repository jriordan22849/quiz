from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def viewqs(request):
	if request.user.is_authenticated():	
		return render(request,'quiz/homepage.html')	
	else: 
		return render(request,'accounts/login.html', {'error':'To view a quiz, please login.'})