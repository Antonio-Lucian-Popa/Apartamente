# apartamente/tasks.py
from apscheduler.schedulers.background import BackgroundScheduler

def initialize_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(actualizeaza_dobanzi, 'interval', days=7)
    scheduler.start()

def actualizeaza_dobanzi():
    from .scrapers import extrage_dobanda_bt, extrage_dobanda_bcr, extrage_dobanda_bnr
    extrage_dobanda_bt()
    extrage_dobanda_bcr()
    extrage_dobanda_bnr()