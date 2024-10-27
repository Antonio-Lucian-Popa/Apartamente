# apartamente/tasks.py
from apscheduler.schedulers.background import BackgroundScheduler
from .scrapers import actualizeaza_dobanzi
import logging

def actualizeaza_dobanzi():
    # Amânăm importul pentru a evita eroarea de inițializare
    from .scrapers import extrage_dobanda_bt, extrage_dobanda_bcr, extrage_dobanda_bnr

    extrage_dobanda_bt()
    extrage_dobanda_bcr()
    extrage_dobanda_bnr()
    logging.info("Dobânzile au fost actualizate.")

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(actualizeaza_dobanzi, 'interval', days=7)
    scheduler.start()