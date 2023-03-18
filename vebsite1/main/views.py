from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

def index(request):
    tasks=Task.objects.all()
    return render(request,'main/index.html',{'title':'Главная страница', 'tasks':tasks})
    # return HttpResponse('<h2>Hello</h2>')
def contact(request):
    return render(request,'main/contact.html')

def about(request):
    return render(request,'main/about.html')

