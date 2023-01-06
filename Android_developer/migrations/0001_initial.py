# Generated by Django 4.1.2 on 2023-01-06 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=63)),
                ('content_type', models.CharField(choices=[('text', 'Текст'), ('image', 'Изображение'), ('table', 'Таблица')], max_length=25, verbose_name='Тип информации')),
                ('content', models.TextField(blank=True, verbose_name='Текст или представление таблицы')),
                ('resource', models.ImageField(blank=True, upload_to='photos/', verbose_name='Изображение')),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=63, verbose_name='Название страницы')),
            ],
            options={
                'verbose_name': 'Страница',
                'verbose_name_plural': 'Страницы',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('width', models.IntegerField(blank=True, default=0)),
                ('height', models.IntegerField(blank=True, default=0)),
                ('border', models.CharField(blank=True, default='0', max_length=25)),
                ('margin', models.CharField(blank=True, default='0', max_length=25)),
                ('others', models.TextField(blank=True)),
                ('content', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Android_developer.content')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('display', models.CharField(choices=[('row', 'Ряд'), ('row-reverse', 'Обратный ряд'), ('column', 'Столбец'), ('column-reverse', 'Обратный столбец')], max_length=25, verbose_name='Отображение')),
                ('order', models.IntegerField(default=0, verbose_name='Место в очереди отображения на странице')),
                ('styles', models.TextField(blank=True)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Android_developer.page')),
            ],
            options={
                'verbose_name': 'Блок информации',
                'verbose_name_plural': 'Блоки',
            },
        ),
        migrations.AddField(
            model_name='content',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Android_developer.section'),
        ),
    ]
