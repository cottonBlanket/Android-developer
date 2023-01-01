from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('MAIN PAGE')


def relevance(request):
    return HttpResponse('Relevance page')


def areas(request):
    return HttpResponse('Areas page')


def competencies(request):
    return HttpResponse('competencies page')


def vacancies(request):
    return HttpResponse('vacancies page')

