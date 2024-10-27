from django.apps import AppConfig
from . import tasks
import threading

class ApartamenteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apartamente'
    def ready(self):
        # from .tasks import start_scheduler
        # threading.Thread(target=start_scheduler).start()
        pass
