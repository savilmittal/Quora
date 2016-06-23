from django import forms
from .models import MyUser

class SignUp(forms.ModelForm):
	username=forms.CharField(max_length=30)
	class Meta:
		model = MyUser
		fields = ['password','contact','email']

class LoginForm(forms.ModelForm):
	username=forms.CharField(max_length=30)
	password=forms.CharField(max_length=20,widget=forms.PasswordInput())
	class Meta:
		model = MyUser
		fields=('username','password',)
		
