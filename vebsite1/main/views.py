from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # return render(request,'')
    return HttpResponse('<h2>Hello</h2>')
def contact(request):
    return HttpResponse('<h2>Контакты</h2>')

def about(request):
    return HttpResponse('<h2>About us</h2>')

