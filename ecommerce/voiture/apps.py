from django.apps import AppConfig


class VoitureConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'voiture'
    
    def ready(sel):
        import voiture.signals
