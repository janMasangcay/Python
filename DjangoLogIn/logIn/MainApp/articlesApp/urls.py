from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path(r'', views.articleList), # http://localhost:8000 - goes to the views.py and run articleList function
    path(r'<slugPutok>/', views.articleDetail),
]
