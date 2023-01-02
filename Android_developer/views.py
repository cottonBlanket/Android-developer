from django.http import HttpResponse
from django.shortcuts import render

navigation = [
    {'name': 'Главная', 'url': 'home'},
    {'name': 'Востребованность', 'url': 'relevance'},
    {'name': 'География', 'url': 'areas'},
    {'name': 'Навыки', 'url': 'competencies'},
    {'name': 'Вакансии', 'url': 'vacancies'},
]


def index(request):
    context = {
        'title': 'Главная страница',
        'navigation': navigation
    }
    return render(request, 'Android-developer/index.html', context=context)


def relevance(request):
    context = {
        'title': 'Востребованность',
        'navigation': navigation
    }
    return render(request, 'Android-developer/relevance.html', context=context)


def areas(request):
    context = {
        'title': 'География',
        'navigation': navigation
    }
    return render(request, 'Android-developer/area.html', context=context)


def competencies(request):
    context = {
        'title': 'Навыки',
        'navigation': navigation
    }
    return render(request, 'Android-developer/competencies.html', context=context)


def vacancies(request):
    context = {
        'title': 'Вакансии',
        'navigation': navigation
    }
    return render(request, 'Android-developer/vacancies.html', context=context)

