from ast import mod
from tkinter import CASCADE
from django.db import models


# Create your models here.
class Exam(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    owner = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    final_grade = models.IntegerField()

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    points = models.IntegerField()
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)

    def __str__(self):
        return self.name