from .models import Task
from django.forms import ModelForm, widgets, TextInput

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title","task","surname"]
        widgets = {"title": TextInput(attrs={'class': 'form-control','placeholder': 'Введите название'}),
                   "task": TextInput(attrs={'class': 'form-control','placeholder': 'Введите описание'}),
                   "surname": TextInput(attrs={'class': 'form-control','placeholder': 'Введите фамилию исполнителя'}),
                   }

