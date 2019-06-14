from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse('This is the home page!')
    return render(request, 'home.html')

def about(request):
    # return HttpResponse('This is the ABOUT page!')
    return render(request, 'about.html')