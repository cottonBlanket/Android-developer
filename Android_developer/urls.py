from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('relevance/', relevance, name='relevance'),
    path('areas/', areas, name='areas'),
    path('competencies/', competencies, name='competencies'),
    path('vacancies/', vacancies, name='vacancies')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
