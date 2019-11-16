from django.apps import AppConfig


class UtilizadoresConfig(AppConfig):
    name = 'utilizadores'
    verbose_name = 'Utilizadores'

    def ready(self):
        import utilizadores.signals
