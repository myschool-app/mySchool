from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Perfil


@receiver(post_save, sender=User)
def criar_perfil(sender, instance, created, **kwargs):
    """
    Cria automaticamente um perfil para cada utilizador
    que se registe na aplicação.
    Um perfil e uma conta de utilizador são modelos separados.
    """
    if created:
        Perfil.objects.create(utilizador=instance)


@receiver(post_save, sender=User)
def guardar_perfil(sender, instance, **kwargs):
    """
    Semelhante à função acima, mas esta apenas guarda o
    perfil quando o mesmo é alterado pelo utilizador.
    """
    instance.perfil.save()
