from django.shortcuts import render, redirect
from .models import Vacancies
from django.http import HttpResponse
import requests
import json
from time import sleep

#from practic.main.models import SearchReq
#from ...practic.main.models import SearchReq
# Create your views here.

user_agent = {'User-Agent': 'MyApp/1.0 (krytoich@gmail.com)'}

def search(request):
    responce = requests.get("https://api.hh.ru/vacancies?text=" + str(request.GET.get("position")))

    if responce.status_code == 200:
        # Сохраняем ответ в файл
        with open('downloaded_file.json', 'wb') as file:
            file.write(responce.content)

    with open('downloaded_file.json', encoding='utf-8') as file:
        data = json.load(file)

    for i in range(5):
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
        elif salary == None:
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

    return redirect('vacans/')

def vacancies_home(request):
    # Удаляем все записи с БД перед поиском
    vacancies1 = Vacancies.objects.all().delete()

    # Функция поиска
    search(request)

    # Получение всех записей с БД
    vacancies1 = Vacancies.objects.all()


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
    return render(request, 'vacancies/vacancies_home.html', {'vacancies1': vacancies1})

