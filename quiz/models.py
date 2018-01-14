from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.forms import ModelForm




class Quiz(models.Model):
    name = models.CharField(max_length=120,default="")
    questions = models.ManyToManyField('Question',related_name='question')



    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Quiz'
        verbose_name_plural='Quizes'


class Question(models.Model):

    question_text=models.CharField(max_length=255)
    answer1= models.CharField(max_length=255)
    answer2= models.CharField(max_length=255)
    answer3= models.CharField(max_length=255)
    correct_answer =models.CharField(max_length=255)


    def __str__(self):
        return self. question_text









