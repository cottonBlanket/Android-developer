from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'Android-developer/index.html', {'title': 'Главная страница'})


def relevance(request):
    return render(request, 'Android-developer/relevance.html', {'title': 'Главная страница'})


def areas(request):
    return render(request, 'Android-developer/area.html', {'title': 'Главная страница'})


def competencies(request):
    return render(request, 'Android-developer/competencies.html', {'title': 'Главная страница'})


def vacancies(request):
    return render(request, 'Android-developer/vacancies.html', {'title': 'Главная страница'})

