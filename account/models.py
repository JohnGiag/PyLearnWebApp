from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils import formats

from codingExercise.models import Exercise
from quiz.models import Quiz


#  ==== Models for Account app ====

class Profile(models.Model):
    """
    The Profile model extends the default User model with extra functionality needed for the project.
    It has 7 fields:
    user(connection with the default User model of Django), points(amount of points ), totalQuizScore,
    quizAvgScore, num_of_copmleted_exercises, num_of_copmleted_quizes and num_of_achievements.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    points = models.IntegerField(default=0)
    totalQuizScore = models.FloatField(default=0)
    quizAvgScore = models.FloatField(default=0)
    num_of_copmleted_exercises = models.IntegerField(default=0)
    num_of_copmleted_quizes = models.IntegerField(default=0)
    num_of_achievements = models.IntegerField(default=0)

    def __str__(self):
        return self.user.get_username()

    def getCompletedQuizes(self, flatFlag):
        """Function that returns a list of all completed quizes for a user """
        if flatFlag:
            completed_quizes = CompletedQuiz.objects.filter(userProfile=self).values_list('quiz_name', flat=flatFlag)
        else:
            completed_quizes = CompletedQuiz.objects.filter(userProfile=self)
        return completed_quizes

    def getCompletedExercises(self, flatFlag):
        """Function that returns a list of all completed exercises for a user """
        if flatFlag:
            completed_exercises = CompletedExercise.objects.filter(userProfile=self).values_list('exercise_name',
                                                                                                 flat=flatFlag)
        else:
            completed_exercises = CompletedExercise.objects.filter(userProfile=self)
        return completed_exercises

    def get_num_of_completed_exercises(self):
        """Function that returns the number of all completed exercises for a user """
        return CompletedExercise.objects.filter(userProfile=self).distinct().count()

    def setAvgQuizSore(self, newScore):
        """Function that calculates the average quiz score for a user """
        self.totalQuizScore += newScore
        tmpCompletedQuizes = self.user.profile.num_of_copmleted_quizes if self.user.profile.num_of_copmleted_quizes > 0 else 1
        self.quizAvgScore = self.totalQuizScore / tmpCompletedQuizes


class CompletedQuiz(models.Model):
    """
    The CompletedQuiz model defines an object to connect a user with a quiz he has completed.
    It has 4 fields userProfile(connection with the Profile model), quiz_name,score,date(date of completion).
    """
    userProfile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    quiz_name = models.CharField(max_length=50, blank=True, null=True)
    score = models.CharField(max_length=10, default="0")
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.quiz_name

    class Meta:
        verbose_name = 'Completed Quiz'
        verbose_name_plural = 'Completed Quizes'


class CompletedExercise(models.Model):
    """
       The CompletedExercise model defines an object to connect a user with a programming exercise he has completed.
       It has 4 fields userProfile(connection with the Profile model), exercise_name, answer, date(date of completion).
       """
    userProfile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    exercise_name = models.CharField(max_length=50, blank=True, null=True)
    answer = models.TextField()
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        formatted_datetime = formats.date_format(self.date, "SHORT_DATETIME_FORMAT")
        return "Exercise: " + self.exercise_name + " on : " + str(formatted_datetime)


import account.meta_badges
