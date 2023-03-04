from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h4>Hello</h4>')

def contact(request):
    return HttpResponse('<h2>Контакты</h2>')
