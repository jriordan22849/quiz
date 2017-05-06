from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout


# Create your views here.
#Check if user exists and login
def loginUser(request):

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username = username, password = password)

		if user is not None:
			login(request, user)
			return render(request,'quiz/homepage.html',{'success': 'User Logged in.'})
		else: 
			return render(request,'accounts/login.html', {'error': 'Username and Password doesnt exist.'})
	else:
		return render(request,'accounts/login.html')
		

# Create your views here.
def signup(request):

	if request.method == 'POST':
		
		if request.POST['password1']  == "" or request.POST['password2'] == "":
			return render(request,'accounts/signup.html', {'error': 'Password fiels is empty'})
			

		#Check if password are the same
		if request.POST['password1'] == request.POST['password2']:

			#check if user name already exits.
			try:
				user = User.objects.get(username = request.POST['username'])
				return render(request,'accounts/signup.html', {'error': 'Username alreasy taken'})
			except User.DoesNotExist:			
				user = User.objects.create_user(request.POST['username'],password = request.POST['password1'])
				login(request,user)
				return render(request,'accounts/signup.html')
		else:
			return render(request,'accounts/signup.html', {'error': 'Passowrd didnt match'})
	else:
		return render(request,'accounts/signup.html')
	

#function to logout a user
def logoutUser(request):
	if request.method == 'POST':
		logout(request)
		return render(request,'accounts/login.html')
		

