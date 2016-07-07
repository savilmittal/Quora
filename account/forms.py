from django import forms
from .models import MyUser

class SignUp(forms.ModelForm):
	username=forms.CharField(max_length=30)
	password=forms.CharField(max_length=20,widget=forms.PasswordInput())
	email=forms.EmailField(max_length=50)
	class Meta:
		model = MyUser
		fields = ['username','password','contact','email']

class LoginForm(forms.ModelForm):
	username=forms.CharField(max_length=30)
	password=forms.CharField(max_length=20,widget=forms.PasswordInput())
	class Meta:
		model = MyUser
		fields=('username','password',)
		
class ChangePassword(forms.Form):
	password=forms.CharField(max_length=20,widget=forms.PasswordInput(),required=True)
	class Meta:
		fields=('password',)
class ForgotPassword(forms.Form):
	token=forms.CharField(required=True)

			