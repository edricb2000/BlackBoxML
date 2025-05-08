# core/views.py
from django.shortcuts import render

def home(request):
    return render(request, "home.html", {}, content_type='text/html')

def docs(request):
    return render(request, "docs.html", {}, content_type='text/html')

