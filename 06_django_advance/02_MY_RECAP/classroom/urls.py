"""my_recap URL Configuration

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
from django.urls import path, include
from . import views

app_name = 'classroom'

urlpatterns = [
    path('', views.index),
    path('students/', views.lists, name='lists'),
    path('students/new/', views.new, name='new'),
    path('students/create/', views.create, name='create'),
    path('students/<int:num>/', views.detail, name='detail'),
    path('students/<int:num>/edit/', views.edit, name='edit'),
    path('students/<int:num>/update/', views.update, name='update'),
    path('students/<int:num>/delete/', views.delete, name='delete'),
]
