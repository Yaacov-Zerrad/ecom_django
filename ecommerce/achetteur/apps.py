from django.apps import AppConfig


class AchetteurConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'achetteur'
    
    def ready(self):
        ''' user is potentiel acheteteur'''
        import achetteur.signals
