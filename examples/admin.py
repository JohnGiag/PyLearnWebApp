from django.contrib import admin
from .models import Example

'''Registering the Example model to have access to edit data from the admin panel.'''
admin.site.register(Example)