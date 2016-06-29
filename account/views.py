from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.http import require_GET,require_POST
from .forms import LoginForm,SignUp
from django.contrib.auth import authenticate,login,logout

@require_GET
def show_login(request):
	if not request.user.is_authenticated():
		f=LoginForm();
		context = { 'f' : f }
		return render(request,'account/login.html',context)
	else:
		return redirect('account.views.user_welcome')


@require_POST
def user_login(request):
	username=request.POST['username']
	password=request.POST['password']
	user=authenticate(username=username,password=password)
	f=LoginForm(request.POST);
	if user:
		login(request,user)
		return redirect('account.views.user_welcome')
	else:
		context = { 'f' : f , 'x':'The username or password is incorrect'}
		return render(request,'account/login.html',context)
		

@require_GET
def show_signup(request):
	if request.user.is_authenticated():
		return redirect('account.views.user_welcome')
	f=SignUp()
	context = {'f':f}
	return render(request,'account/signup.html',context)

@require_POST
def user_signup(request):
	f=SignUp(request.POST)
	if f.is_valid():
		user=f.save(commit=False)
		user.set_password(f.cleaned_data['password'])
		user.save()
		return HttpResponse("submission successful!")
	context={'f':f}
	return render(request,'account/signup.html',context)

@login_required
def user_welcome(request):
	return render(request,'account/welcome.html')


@login_required
def user_logout(request):
	logout(request)
	return redirect('account.views.show_login')




	





