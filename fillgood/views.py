from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'fillgood/index.html')

def survey(request):
    return render(request, 'fillgood/survey.html')

def nutritionary(request):
    return render(request, 'fillgood/nutritionary.html')

def article(request):
    return render(request, 'fillgood/article.html')

def write(request):
    return render(request, 'fillgood/write.html')

def login(request):
    return render(request, 'fillgood/login.html')

def signin(request):
    return render(request, 'fillgood/signin.html')