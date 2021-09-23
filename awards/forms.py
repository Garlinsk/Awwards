from django import forms
from .models import *

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        exclude = ['Author', 'pub_date', 'author_profile']
        widgets = {
            'project_description': forms.Textarea(attrs={'rows': 4, 'cols': 10, }),
        }
