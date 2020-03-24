from django.contrib.auth.models import User
from django.db import models


class Perfil(models.Model):
  """
  Objeto Perfil, responsável por armazenar informação relativa ao perfil
  de cada utilizador da aplicação.
  Quando um utilizador se regista na aplicação, um perfil é criado
  automaticamente.
  """
  utilizador = models.OneToOneField(User, on_delete=models.CASCADE)

  def __str__(self):
    return f'Perfil de {self.utilizador.username}'

  class Meta:
    verbose_name = 'Perfil'
    verbose_name_plural = 'Perfis'
