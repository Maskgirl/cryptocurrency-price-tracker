from django.apps import AppConfig


class PriceTrackerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'price_tracker'

    def ready(self):
        from .utils import check_price_scheduler
        check_price_scheduler()
