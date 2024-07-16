from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Vacancies
from django.http import HttpResponse
import requests
import json
from time import sleep
import os
from django.views.generic import ListView

#from practic.main.models import SearchReq
#from ...practic.main.models import SearchReq
# Create your views here.
from main import views

user_agent = {'User-Agent': 'MyApp/1.0 (krytoich@gmail.com)'}



def vacancies_home(request):
    # Удаляем все записи с БД перед поиском

    # Функция поиска
    #search(request)




    # Получение всех записей с БД
    vacancies1 = Vacancies.objects.all()

    paginator = Paginator(vacancies1, 2)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    # Работа с GET запросом отправляемым с формы на главном экране
    print(request.GET.get("position"))
    print(request.GET.get("exp"))
    print(request.GET.get("workForm"))
    print(request.GET.get("workForm1"))
    print(request.GET.get("workForm2"))
    print(request.GET.get("workForm3"))
    print(request.GET.get("workForm4"))
    print(request.GET.get("slider"))




    # Отправление с ранее полученых данных БД в шаблон HTML
    return render(request, 'vacancies/vacancies_home.html', {'page_obj': page_obj,'vacancies1': vacancies1})
