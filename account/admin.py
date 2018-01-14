from django.contrib import admin
from .models import Profile, CompletedQuiz, CompletedExercise


# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'points']


class CompletedQuizAdmin(admin.ModelAdmin):
    list_display = ['userProfile', 'quiz_name', 'score', 'date']


class CompletedExerciseAdmin(admin.ModelAdmin):
    list_display = ['userProfile', 'exercise_name', 'date']


admin.site.register(Profile, UserProfileAdmin)
admin.site.register(CompletedQuiz, CompletedQuizAdmin)
admin.site.register(CompletedExercise, CompletedExerciseAdmin)
