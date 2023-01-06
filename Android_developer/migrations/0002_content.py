# Generated by Django 4.1.2 on 2023-01-05 21:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Android_developer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('content_type', models.CharField(choices=[('Текст', 1), ('Изображение', 2), ('Таблица', 3)], max_length=25)),
                ('resource', models.ImageField(upload_to='')),
                ('content', models.TextField()),
                ('order', models.IntegerField()),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Android_developer.page')),
            ],
        ),
    ]
