from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.http import require_GET,require_POST
from .forms import LoginForm,SignUp
from django.contrib.auth import authenticate,login

@require_GET
def show_login(request):
	if not request.user.is_authenticated():
		f=LoginForm();
		context = { 'f' : f }
		return render(request,'account/login.html',context)
	else:
		return HttpResponse("welcome")

@require_POST
def user_login(request):
	username=request.POST['username']
	password=request.POST['password']
	user=authenticate(username=username,password=password)
	if user:
		login(request,user)
		return HttpResponse("welcome page")
	else:
		return HttpResponse("invalid user and show login page with errors ")
		

@require_GET
def show_signup(request):
	if request.user.is_authenticated():
		return HttpResponse("welcome page")
	f=SignUp()
	context = {'f':f}
	return render(request,'account/signup.html',context)







