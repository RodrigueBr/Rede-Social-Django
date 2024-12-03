from django.apps import AppConfig

class AplicConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'aplic'

class AplicConfig(AppConfig):
    name = 'aplic'

    def ready(self):
        import aplic.signals