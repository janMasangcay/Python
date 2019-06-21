"""MainApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include # to be able to map MainApp urls.py to other Apps urls.py (ex. line 24)
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 

urlpatterns = [
    path('putok/', admin.site.urls), # http://localhost:8000/admin/
    path('', views.homePage), # http://localhost:8000
    path('about/', views.about), # http://localhost:8000/about
    path('articles/', include('articlesApp.urls')), # This tells django that if I type localhost://8000/articles/ - it'll look for articlesApp.urls
]

urlpatterns += staticfiles_urlpatterns()

# from django.contrib.staticfiles.urls import staticfiles_urlpatterns - tells Django to serve our static files for us.
