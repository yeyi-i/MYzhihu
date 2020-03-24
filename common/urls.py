from django.urls import path
from . import views

urlpatterns = [
    path('question/', views.question, name='question'),
    path('index/', views.index, name='index'),
]
