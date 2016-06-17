from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
	contact=models.CharField(max_length=10,null=True)



