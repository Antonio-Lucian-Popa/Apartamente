# apartamente/apps.py
from django.apps import AppConfig
from django.db.models.signals import post_migrate
import threading

class ApartamenteConfig(AppConfig):
    name = 'apartamente'

    def ready(self):
        post_migrate.connect(start_scheduler, sender=self)
        
def start_scheduler(sender, **kwargs):
    from .tasks import initialize_scheduler
    threading.Thread(target=initialize_scheduler).start()