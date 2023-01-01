from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('relevance/', relevance, name='relevance'),
    path('areas/', areas, name='areas'),
    path('competencies/', competencies, name='competencies'),
    path('vacancies/', vacancies, name='vacancies')
]
