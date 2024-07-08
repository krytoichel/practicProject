import requests
import json
from time import sleep

user_agent = {'User-Agent': 'MyApp/1.0 (krytoich@gmail.com)'}


responce = requests.get("https://api.hh.ru/vacancies?text=python")
print(responce.status_code)

if responce.status_code == 200:
    # Сохраняем ответ в файл
    with open('downloaded_file.json', 'wb') as file:
        file.write(responce.content)

with open('downloaded_file.json', encoding='utf-8') as file:
    data = json.load(file)

# Теперь переменная 'data' содержит словарь с данными из файла
# print(data)

# for i in range(10):
#     item_name = data['items'][i]['name']
#     item_id = data['items'][i]['id']
#     string_representation = str(data['items'][i]['salary']['from'])
#     item_salary = string_representation+".."+str(data['items'][i]['salary']['to'])+" "+data['items'][i]['salary']['currency']
#     item_comp = data['items'][i]['employer']['name']
#     item_addres = data['items'][i]['address']
#     if item_addres == None:
#         item_addres = data['items'][i]['area']['name']

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
    elif salary == None:
        salary = "Не указана"

    sleep(1)

# print(item_id)
# print(item_name)
# print(item_salary)
# print(item_comp)
# print(item_addres)

    values = {
        "id": id,
        "position": position,
        "salary":salary,
        "comp":comp,
        "adr":addres
    }

    print(values)