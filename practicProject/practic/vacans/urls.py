from django.urls import path
from . import views

urlpatterns = [
    path('', views.vacancies_home),
]

