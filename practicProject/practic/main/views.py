import json
import os
from time import sleep

import requests
from django.shortcuts import render, redirect
from django.apps import apps
from django.http import HttpResponse
from .models import SearchReq
from .forms import SearchReqForm
from vacans.models import Vacancies

s = 0


def search(request):
    p = str(request.GET.get("position"))
    if p != 'None' or p != None:
        r = []
        r.append(p)
        print(r)
        print("https://api.hh.ru/vacancies?text="+r[0])
        responce = requests.get("https://api.hh.ru/vacancies?text="+r[0])
    # str(request.GET.get("position"))


    if responce.status_code == 200:
        # Сохраняем ответ в файл
        with open('vacans/downloaded_file.json', 'w', encoding='utf-8') as file:
            file.write(responce.text)

    with open('vacans/downloaded_file.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    for i in range(len(data['items'])):
        item = data['items'][i]
        salary = item['salary']
        position = item['name']
        id = item['id']
        comp = item['employer']['name']
        addres = item['address']

        if addres == None:
            addres = item['area']['name']

        # Проверяем, что 'from' существует и не равно None
        if salary != None:
            if salary['from'] is not None:
                # Если 'from' существует и имеет значение, выводим его
                salary['from'] = salary['from']
            else:
                # В противном случае выводим сообщение об отсутствии значения
                salary['from'] = "0"
        elif salary is None:
            salary = "Не указана"

        sleep(1)
        # Запись в БД одной вакансии
        vacancies = Vacancies(job_title=position, salary=salary,
                              company=comp, city=addres)
        vacancies.save()

    # id = 122125
    # position = "Python dev"
    # salary = 150000
    # comp = "Google"
    # addres = "Mahachkala"


    values = {
        "id": id,
        "position": position,
        "salary": salary,
        "comp": comp,
        "adr": addres
    }

    redirect("vacans/")

search.is_complete = False


# Create your views here.

def index(request):
    print("YYYYY")





def create(request):
    form = SearchReqForm()
    error = ''
    data = {
        'form': form,
        'error': error,
    }

    if request.method == "GET":
        print(request.GET.get("position"))
        if request.GET.get("position") == None:
            print("Он тут")
        else:
            if os.path.exists('vacans/downloaded_file.json'):
                # Удаляем файл
                os.remove('vacans/downloaded_file.json')
                print('Удаление файла.')

            Vacancies.objects.all().delete()

            search(request)
            search.is_complete = True

        if search.is_complete:
            return redirect("vacans/")
        else:
            return render(request, 'main/index.html', data)

