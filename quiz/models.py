from django.db import models

from codingExercise.models import Chapter


# Create your models here.




class Quiz(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, blank=True, null=True)
    order = models.IntegerField(null=True,default=0)
    name = models.CharField(max_length=120, default="")
    # questions = models.ManyToManyField('Question', related_name='question')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Quiz'
        verbose_name_plural = 'Quizes'

        ordering = ['order']


class Question(models.Model):
    quiz =models.ForeignKey(Quiz,on_delete=models.CASCADE,null=True)
    question_text = models.TextField()
    answer1 = models.CharField(max_length=255)
    answer2 = models.CharField(max_length=255)
    answer3 = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=255)

    def __str__(self):
        return self.question_text
