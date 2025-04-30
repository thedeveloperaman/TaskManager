from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    """
    Form for creating and updating Task instances.
    """
    class Meta:
        model = Task
        fields = ['title', 'category']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Task title',
                'class': 'form-control',
                'maxlength': 255,
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
            }),
        }
