# apartamente/utils.py
from .models import Dobanda

def calcul_rata(principal, banca, durata_ani=20):
    try:
        dobanda_obj = Dobanda.objects.get(banca=banca)
        dobanda = float(dobanda_obj.dobanda) / 100
    except Dobanda.DoesNotExist:
        dobanda_obj = Dobanda.objects.get(banca="BNR")
        dobanda = float(dobanda_obj.dobanda) / 100

    durata_luni = durata_ani * 12
    rata_dobanda = dobanda / 12
    rata_lunara = (principal * rata_dobanda * (1 + rata_dobanda) ** durata_luni) / ((1 + rata_dobanda) ** durata_luni - 1)
    return rata_lunara