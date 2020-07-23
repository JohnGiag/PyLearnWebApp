from django.contrib import admin
from .models import Exercise,Chapter
from .forms import  ExerciseAdminForm

'''Registering the Exercise and Chapter models to have access to edit data from the admin panel.'''

class ExerciseAdmin(admin.ModelAdmin):
    form = ExerciseAdminForm

admin.site.register(Exercise,ExerciseAdmin)
admin.site.register(Chapter)