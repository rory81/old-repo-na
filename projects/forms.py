from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'title',
            'category',
            'description',
            'backers_story',
            'goal',
            'end_date'
        ]
