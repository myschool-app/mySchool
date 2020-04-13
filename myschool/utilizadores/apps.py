from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UtilizadoresConfig(AppConfig):
    name = 'utilizadores'
    verbose_name = _('Utilizadores')

    def ready(self):
        pass
