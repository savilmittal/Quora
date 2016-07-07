from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class MyUser(AbstractUser):
	contact=models.BigIntegerField(blank=False,validators=[RegexValidator(regex='^.{10}$', message='Please enter a valid contact', code='nomatch')])
	token=models.CharField(blank=False,max_length=4,default='')
	def __str__(self):
		return self.username



