from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import calcul_rata

# Create your views here.
class RataCalculator(APIView):
    def get(self, request, pret_apartament, banca, durata_ani=20):
        rata_lunara = calcul_rata(pret_apartament, banca, durata_ani)
        
        response_data = {
            "rata_lunara": rata_lunara,
            "banca": banca,
            "durata_ani": durata_ani
        }
        return Response(response_data)