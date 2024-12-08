from django.contrib.auth.models import AbstractUser
from django.db import models


class UserCustom(AbstractUser):
    age = models.CharField(max_length=3)
    date_of_birth = models.DateField()

