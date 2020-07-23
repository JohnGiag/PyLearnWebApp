from django.contrib import admin
from .models import Quiz,Question

'''Registering the Quiz and Question models to have access to edit data from the admin panel.'''

admin.site.register(Quiz)

admin.site.register(Question)
