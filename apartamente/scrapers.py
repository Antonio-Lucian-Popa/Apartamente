# apartamente/scrapers.py
import requests
from bs4 import BeautifulSoup
from .models import Dobanda

def extrage_dobanda_bt():
    url = "https://www.bancatransilvania.ro/personal/credite/credit-ipotecar/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    dobanda = float(soup.select_one('.dobanda-text').text.replace('%', '').strip())
    Dobanda.objects.update_or_create(banca="Banca Transilvania", defaults={"dobanda": dobanda})

def extrage_dobanda_bcr():
    url = "https://www.bcr.ro/ro/persoane-fizice/credite/credite-ipotecare"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    dobanda = float(soup.select_one('.dobanda').text.replace('%', '').strip())
    Dobanda.objects.update_or_create(banca="BCR", defaults={"dobanda": dobanda})

def extrage_dobanda_bnr():
    url = "https://www.bnr.ro/Moneda-naţională-1574.aspx"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    dobanda = float(soup.select_one(".rate-cell").text.strip().replace('%', ''))
    Dobanda.objects.update_or_create(banca="BNR", defaults={"dobanda": dobanda})

def actualizeaza_dobanzi():
    extrage_dobanda_bt()
    extrage_dobanda_bcr()
    extrage_dobanda_bnr()