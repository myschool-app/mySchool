from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

# Professor


class Professor(models.Model):
    utilizador = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name=_('Utilizador'))
    nome = models.CharField(max_length=50, verbose_name=_('Nome'))
    email = models.EmailField(verbose_name=_('Endereço de Email'), blank=True)
    telefone = models.CharField(
        max_length=20, verbose_name=_('Telefone'), blank=True)

    class Meta:
        verbose_name = _('Professor')
        verbose_name_plural = _('Professores')

    def __str__(self):
        return self.nome


# Disciplina


class Disciplina(models.Model):
    utilizador = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name=_('Utilizador'))
    descricao = models.CharField(max_length=50, verbose_name=_('Descrição'))
    professor = models.ForeignKey(
        'Professor', on_delete=models.SET_NULL, blank=True, null=True, verbose_name=_('Professor'))

    class Meta:
        verbose_name = _('Disciplina')
        verbose_name_plural = _('Disciplinas')

    def get_absolute_url(self):
        return reverse('app-disciplinas-editar', kwargs={'pk': self.pk})

    def __str__(self):
        return self.descricao

# Teste


class Teste(models.Model):
    utilizador = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name=_('Utilizador'))
    disciplina = models.ForeignKey(
        'Disciplina', on_delete=models.CASCADE, verbose_name=_('Disciplina'))
    data = models.DateField(verbose_name=_('Data'))
    notas = models.TextField(
        max_length=255, blank=True, verbose_name=_('Notas'))
    realizado = models.BooleanField(
        verbose_name=_('Realizado?'), blank=True, null=True)
    avaliacao = models.FloatField(
        verbose_name=_('Avaliação'), blank=True, null=True)

    class Meta:
        verbose_name = _('Teste')
        verbose_name_plural = _('Testes')

    def __str__(self):
        return self.disciplina.descricao

# Evento


class Evento(models.Model):
    utilizador = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name=_('Utilizador'))
    titulo = models.CharField(max_length=50, verbose_name=_('Título'))
    descricao = models.CharField(max_length=255, verbose_name=_('Descrição'))
    data_inicio = models.DateTimeField(verbose_name=_('Data de Início'))
    data_fim = models.DateTimeField(verbose_name=_('Data de Fim'))

    class Meta:
        verbose_name = _('Evento')
        verbose_name_plural = _('Eventos')

    def __str__(self):
        return self.titulo
