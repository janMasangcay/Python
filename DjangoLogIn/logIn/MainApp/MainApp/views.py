from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    return render(request, 'homePage.html')

def about(request):
    return render(request, 'about.html')