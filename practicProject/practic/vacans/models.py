from django.db import models

# Create your models here.

class Vacancies(models.Model):
    job_title = models.CharField('Должность', max_length=50)
    salary = models.CharField('Зарплата',max_length=6)
    company = models.CharField('Компания',max_length=45)
    city = models.CharField('Город',max_length=20)

    def __str__(self):
        return self.job_title

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'