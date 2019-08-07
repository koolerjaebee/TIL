from django.urls import path
from . import views

urlpatterns = [
    path('start/', views.start),
    path('end/', views.end),
]
