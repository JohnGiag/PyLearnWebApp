from django.db import models

from codingExercise.models import Chapter


# Create your models here.


class Quiz(models.Model):
    """
    The Quiz model is used to create an object that models a collection of multiple choice questions.
    It has 3 fields, chapter (the Chapter it belongs to), order (a field used show the order in witch an exercise should
    be completed), name.
    """
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, blank=True, null=True)
    order = models.IntegerField(null=True, default=0)
    name = models.CharField(max_length=120, default="")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Quiz'
        verbose_name_plural = 'Quizes'
        ordering = ['order']


class Question(models.Model):
    """
      The Question model is used to create an object that models a  multiple choice question with 3 possible answers.
      It has 6 fields, quiz (the Quiz it belongs to), question_text, answer1, answer2, answer3 and correct_answer.
    """
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True)
    question_text = models.TextField()
    answer1 = models.CharField(max_length=255)
    answer2 = models.CharField(max_length=255)
    answer3 = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=255)

    def __str__(self):
        return self.question_text
