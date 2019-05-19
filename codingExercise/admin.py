from django.contrib import admin
from .models import Exercise,Chapter
from .forms import  ExerciseAdminForm

# Register your models here.

class ExerciseAdmin(admin.ModelAdmin):
    form = ExerciseAdminForm

admin.site.register(Exercise,ExerciseAdmin)
admin.site.register(Chapter)