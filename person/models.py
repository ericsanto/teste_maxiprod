from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)


