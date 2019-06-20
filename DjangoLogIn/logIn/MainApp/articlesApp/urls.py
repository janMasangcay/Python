from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.articleList, name = 'listAnglit'), # http://localhost:8000/articles/ - goes to the views.py and run articleList function
    path('<slugPutok>/', views.articleDetail),
]
