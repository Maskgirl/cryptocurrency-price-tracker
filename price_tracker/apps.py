from django.apps import AppConfig
from django.core.mail import send_mail


class PriceTrackerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'price_tracker'

    def ready(self):
        from .utils import scheduler
        scheduler.start()
