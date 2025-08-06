from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class WebUser(models.Model):
    username = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)
