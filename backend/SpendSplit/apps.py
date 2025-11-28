from django.apps import AppConfig


class SpendsplitConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'SpendSplit'

    def ready(self):
        import SpendSplit.signals