# Generated by Django 4.1.2 on 2023-01-09 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Android_developer', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='content',
            options={'verbose_name': 'Содержание блока', 'verbose_name_plural': 'Содержание'},
        ),
        migrations.AlterModelOptions(
            name='style',
            options={'verbose_name': 'Стили', 'verbose_name_plural': 'Стили'},
        ),
        migrations.AddField(
            model_name='section',
            name='title_styles',
            field=models.TextField(blank=True),
        ),
    ]