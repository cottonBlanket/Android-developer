import enum

from django.db import models

CONTENT_TYPES = (
    ('text', 'Текст'),
    ('image', 'Изображение'),
    ('table', 'Таблица'),
)

PAGES = (
    ('home', 'Главная'),
    ('relevance', 'Восстребованность'),
    ('areas', 'География'),
    ('competencies', 'Навыки'),
    ('vacancies', 'Вакансии')
)


class Content(models.Model):
    title = models.CharField(max_length=63, blank=True)
    section = models.ForeignKey('Section', on_delete=models.CASCADE)
    content_type = models.CharField(max_length=25, choices=CONTENT_TYPES, verbose_name="Тип информации")
    content = models.TextField(blank=True, verbose_name="Текст или представление таблицы")
    resource = models.ImageField(upload_to="photos/", blank=True, verbose_name="Изображение")
    title_styles = models.TextField(blank=True, verbose_name="CSS стили для заголовка")
    style = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.section}. {self.content_type}'

    class Meta:
        verbose_name = 'Содержание блока'
        verbose_name_plural = 'Содержание'
        ordering = ['section']


class Section(models.Model):
    page = models.CharField(max_length=25, choices=PAGES)
    order = models.IntegerField(verbose_name="Место в очереди отображения на странице", default=0)
    title = models.CharField(max_length=255)
    title_styles = models.TextField(blank=True, null=True)
    styles = models.TextField(blank=True, verbose_name="CSS стили для блока")


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блок информации'
        verbose_name_plural = 'Блоки'
        ordering = ['page', 'order']

