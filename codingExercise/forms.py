from .models import Exercise
from django import forms
from django_ace import AceWidget


class ExerciseAdminForm(forms.ModelForm):
    class Meta:
        model = Exercise
        widgets = {
            "test_imports": AceWidget(theme='twilight', mode='python', wordwrap=True, width='100%'),
            "test": AceWidget(theme='twilight', mode='python', wordwrap=True, width='100%'),
            "text": AceWidget(theme='twilight', mode='python', wordwrap=True, width='100%'),

        }
        fields = "__all__"


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        widgets = {
            "text": AceWidget(theme='twilight', mode='python', wordwrap=True, width='100%'),

        }
        fields = ['text']
