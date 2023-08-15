from django import forms
from todo_app.models import TaskModel

class TodoForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['taskTitle','taskDescription',]