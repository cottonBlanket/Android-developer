from django.shortcuts import render
from .models import *


def get_orders(page_id):
    orders = sorted(list(map(lambda x: x.order, Content.objects.filter(page=page_id))))
    return orders


def get_page_context(page_id: int):
    navigation = [
        {'name': 'Главная', 'url': 'home'},
        {'name': 'Востребованность', 'url': 'relevance'},
        {'name': 'География', 'url': 'areas'},
        {'name': 'Навыки', 'url': 'competencies'},
        {'name': 'Вакансии', 'url': 'vacancies'},
    ]
    context = {'navigation': navigation,
               'title': Page.objects.get(pk=page_id).title,
               'orders': get_orders(page_id),
               'page_id': page_id}
    return context


def index(request):
    context = get_page_context(1)
    return render(request, 'Android-developer/index.html', context=context)


def relevance(request):
    context = get_page_context(2)
    return render(request, 'Android-developer/relevance.html', context=context)


def areas(request):
    context = get_page_context(3)
    return render(request, 'Android-developer/area.html', context=context)


def competencies(request):
    context = get_page_context(4)
    return render(request, 'Android-developer/competencies.html', context=context)


def vacancies(request):
    context = get_page_context(5)
    return render(request, 'Android-developer/vacancies.html', context=context)
