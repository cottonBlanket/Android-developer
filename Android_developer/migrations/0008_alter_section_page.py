# Generated by Django 4.1.2 on 2023-01-14 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Android_developer', '0007_remove_style_content_remove_content_order_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='page',
            field=models.CharField(choices=[('home', 'Главная'), ('relevance', 'Восстребованность'), ('areas', 'География'), ('competencies', 'Навыки'), ('vacancies', 'Вакансии')], max_length=25),
        ),
    ]
