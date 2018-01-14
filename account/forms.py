from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control','placeholder':'Enter your password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control','placeholder':'Enter your password again'}))

    class Meta:
        model = User
        fields = ['username','email']
        widgets = {

            'username':forms.TextInput(attrs={'class' : 'form-control','placeholder':'Enter your username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder':'Enter your email'}),


        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password2'] != cd['password']:
            raise ValidationError('Passwords don\'t match')

        return cd['password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError(u'An account has already been created with this email address')
        return email


