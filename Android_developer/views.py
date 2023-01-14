from django.shortcuts import render
from .models import *
from .logic import vacancies_loader


def get_page_context(page):
    navigation = [
        {'name': 'Главная', 'url': 'home'},
        {'name': 'Востребованность', 'url': 'relevance'},
        {'name': 'География', 'url': 'areas'},
        {'name': 'Навыки', 'url': 'competencies'},
        {'name': 'Вакансии', 'url': 'vacancies'},
    ]
    context = {'navigation': navigation,
               'sections': sorted(Section.objects.filter(page=page), key=lambda x: x.order)}
    return context


def index(request):
    context = get_page_context('home')
    return render(request, 'Android-developer/index.html', context=context)


def relevance(request):
    context = get_page_context('relevance')
    return render(request, 'Android-developer/relevance.html', context=context)


def areas(request):
    context = get_page_context('areas')
    return render(request, 'Android-developer/area.html', context=context)


def competencies(request):
    context = get_page_context('competencies')
    return render(request, 'Android-developer/competencies.html', context=context)


def vacancies(request):
    context = get_page_context('vacancies')
    context['vacancies'] = vacancies_loader.get_data()
    return render(request, 'Android-developer/vacancies.html', context=context)
