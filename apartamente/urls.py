# apartamente/urls.py
from django.urls import path
from .views import RataCalculator

urlpatterns = [
    path('rata/<int:pret_apartament>/<str:banca>/', RataCalculator.as_view(), name='rata-calculator-default'),
    path('rata/<int:pret_apartament>/<str:banca>/<int:durata_ani>/', RataCalculator.as_view(), name='rata-calculator'),
]