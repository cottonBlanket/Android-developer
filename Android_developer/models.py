from django.db import models


class Statistic(models.Model):
    key = models.CharField(max_length=25)
    info = models.CharField(max_length=25, default='all')
    salary = models.IntegerField()
    count = models.FloatField()


class Vacancy(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    skills = models.ManyToManyField('Skill')
    salary = models.IntegerField(verbose_name="Оклад")
    city = models.CharField(max_length=25, verbose_name="Город")
    published = models.DateTimeField(verbose_name="Дата публикации")


class Skill(models.Model):
    name = models.CharField(max_length=63, verbose_name='Навык')
    vacancies = models.ManyToManyField('Vacancy')

# class CityStatistic(models.Model):
#     name = models.CharField(max_length=25)
#     salary = models.IntegerField()
#     count = models.FloatField()
#
#
# class YearStatistic(models.Model):
#     year = models.DateField()
#     salary = models.IntegerField()
#     count = models.FloatField()


