import enum

from django.db import models

CONTENT_TYPES = (
    ('text', 'Текст'),
    ('image', 'Изображение'),
    ('table', 'Таблица'),
)


class Content(models.Model):
    title = models.CharField(max_length=25, verbose_name="Заголовок")
    page = models.ForeignKey('Page', on_delete=models.CASCADE)
    content_type = models.CharField(max_length=25, choices=CONTENT_TYPES, verbose_name="Тип информации")
    content = models.TextField(blank=True, verbose_name="Текст или представление таблицы")
    resource = models.ImageField(upload_to="photos/", blank=True, verbose_name="Изображение")
    order = models.IntegerField(verbose_name="Место в очереди отображения на странице")

    def __str__(self):
        return self.title


# class Text(models.Model):
#     title = models.CharField(max_length=25)
#     page = models.ForeignKey('Page', on_delete=models.CASCADE)
#     content = models.TextField()
#     order = models.IntegerField()
#
#     def __str__(self):
#         return self.title
#
#
# class Image(models.Model):
#     title = models.CharField(max_length=25)
#     page = models.ForeignKey('Page', on_delete=models.CASCADE)
#     content = models.ImageField()
#     order = models.IntegerField()
#
#     def __str__(self):
#         return self.title
#
#
# class Table(models.Model):
#     title = models.CharField(max_length=25)
#     page = models.ForeignKey('Page', on_delete=models.CASCADE)
#     # page = models.ForeignKey('Page', on_delete=models.PROTECT)
#     headers = models.TextField()
#     content = models.TextField()
#     order = models.IntegerField()
#
#     def __str__(self):
#         return self.title


class Page(models.Model):
    title = models.CharField(max_length=63, verbose_name="Название страницы")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'
        ordering = ['pk']


# class Statistic(models.Model):
#     key = models.CharField(max_length=25)
#     info = models.CharField(max_length=25, default='all')
#     salary = models.IntegerField()
#     count = models.FloatField()
#
#
# class Vacancy(models.Model):
#     name = models.CharField(max_length=255, verbose_name='Название')
#     skills = models.TextField()
#     salary = models.IntegerField(verbose_name="Оклад")
#     city = models.CharField(max_length=25, verbose_name="Город")
#     published = models.DateTimeField(verbose_name="Дата публикации")




