from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class MyUser(AbstractUser):
	contact=models.BigIntegerField(max_length=10,blank=False,validators=[RegexValidator(regex='^.{10}$', message='Please enter a valid contact', code='nomatch')])

	def __str__(self):
		return self.username



