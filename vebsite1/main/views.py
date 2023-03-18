from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

from .forms import TaskForm

def index(request):
    tasks=Task.objects.all()
    return render(request,'main/index.html',{'title':'Главная страница', 'tasks':tasks})
    # return HttpResponse('<h2>Hello</h2>')
def contact(request):
    return render(request,'main/contact.html')

def about(request):
    return render(request,'main/about.html')

def create(request):
    form = TaskForm()
    context={
        'form': form
    }
    return render(request,'main/create.html')

