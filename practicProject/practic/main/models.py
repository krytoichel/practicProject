from django.db import models
import django.utils.encoding

from django.utils.encoding import smart_str

# Create your models here.

class SearchReq(models.Model):
    position = models.CharField('Должность',max_length=50)
    exp = models.CharField('Опыт', max_length=3)
    workForm = models.CharField('ФорматРаботы', max_length=20)
    workForm1 = models.CharField('ФорматРаботы', max_length=20)
    workForm2 = models.CharField('ФорматРаботы', max_length=20)
    workForm3 = models.CharField('ФорматРаботы', max_length=20)
    workForm4 = models.CharField('ФорматРаботы', max_length=20)
    salary = models.CharField('Зарплата', max_length=7)

    def __str__(self):
        return self.position


    class Meta:
        verbose_name = 'Поисковой запрос'
        verbose_name_plural = 'Поисковые запросы'