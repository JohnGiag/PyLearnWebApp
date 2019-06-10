from django import forms

from .models import Quiz, Question


class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['name']


class QuestionForm(forms.ModelForm):
    answer1 = forms.MultipleChoiceField()
    answer2 = forms.MultipleChoiceField()
    answer3 = forms.MultipleChoiceField()

    class Meta:
        model = Question
        fields = '__all__'

# TO DELETE
