from django import forms
from .models import *
from registration.forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        exclude = ['Author', 'pub_date', 'author_profile']
        widgets = {
            'project_description': forms.Textarea(attrs={'rows': 4, 'cols': 10, }),
        }
class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        exclude = ['user']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 2, 'cols': 10, }),
        }


class RegisterForm(RegistrationForm):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2',)

    widgets = {
        'first_name': forms.TextInput(attrs={'class': 'form-control names', 'placeholder': "First Name", 'label': 'First Name'}),
        'last_name': forms.TextInput(attrs={'class': 'form-control names', 'placeholder': "Second Name", 'label': 'Second Name'}),
        'email': forms.TextInput(attrs={'class': 'form-control names', 'placeholder': "Email Address", 'label': 'Email Address'}),
        'username': forms.TextInput(attrs={'class': 'form-control names', 'placeholder': "Username", 'label': 'Username'}),
        'password1': forms.PasswordInput(attrs={'class': 'form-control ', 'type': 'password', 'placeholder': "Password", 'label': 'Password'}),
        'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Confirm Password", 'label': 'Confirm Password'}),
    }
