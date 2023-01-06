import enum

from django.db import models

CONTENT_TYPES = (
    ('text', 'Текст'),
    ('image', 'Изображение'),
    ('table', 'Таблица'),
)

FLEX_DIRECTION = (
    ('row', 'Ряд'),
    ('row-reverse', 'Обратный ряд'),
    ('column', 'Столбец'),
    ('column-reverse', 'Обратный столбец')
)


class Style(models.Model):
    content = models.OneToOneField('Content', on_delete=models.CASCADE)
    width = models.IntegerField(default=0, blank=True)
    height = models.IntegerField(default=0, blank=True)
    border = models.CharField(max_length=25, default='0', blank=True)
    margin = models.CharField(max_length=25, default='0', blank=True)
    others = models.TextField(blank=True)

    def __str__(self):
        return f'Стили для {self.content.section}'

    class Meta:
        verbose_name = 'Стили'
        verbose_name_plural = 'Стили'


class Content(models.Model):
    title = models.CharField(max_length=63, blank=True)
    section = models.ForeignKey('Section', on_delete=models.CASCADE)
    content_type = models.CharField(max_length=25, choices=CONTENT_TYPES, verbose_name="Тип информации")
    content = models.TextField(blank=True, verbose_name="Текст или представление таблицы")
    resource = models.ImageField(upload_to="photos/", blank=True, verbose_name="Изображение")

    def __str__(self):
        return f'{self.section}. {self.content_type}'

    class Meta:
        verbose_name = 'Содержание блока'
        verbose_name_plural = 'Содержание'


class Section(models.Model):
    title = models.CharField(max_length=255)
    page = models.ForeignKey('Page', on_delete=models.CASCADE)
    display = models.CharField(max_length=25, choices=FLEX_DIRECTION, verbose_name="Отображение")
    order = models.IntegerField(verbose_name="Место в очереди отображения на странице", default=0)
    styles = models.TextField(blank=True)

    def __str__(self):
        return self.title + '. ' + self.page.title

    class Meta:
        verbose_name = 'Блок информации'
        verbose_name_plural = 'Блоки'


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




