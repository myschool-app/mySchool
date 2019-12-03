from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Professor


class Professor(models.Model):
    utilizador = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50, verbose_name="Nome")
    email = models.EmailField(verbose_name="Endereço de Email", blank=True)
    telefone = models.CharField(
        max_length=20, verbose_name="Telefone", blank=True)

    class Meta:
        verbose_name = "Professor"
        verbose_name_plural = "Professores"

    def __str__(self):
        return self.nome


# Disciplina


class Disciplina(models.Model):
    utilizador = models.ForeignKey(User, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=50, verbose_name="Descrição")
    professor = models.ForeignKey(
        'Professor', on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Professor")

    class Meta:
        verbose_name = "Disciplina"
        verbose_name_plural = "Disciplinas"

    def get_absolute_url(self):
        return reverse('app-disciplinas-editar', kwargs={'pk': self.pk})

    def __str__(self):
        return self.descricao

# Teste


class Teste(models.Model):
    utilizador = models.ForeignKey(User, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(
        'Disciplina', on_delete=models.CASCADE, verbose_name="Disciplina")
    data = models.DateField(verbose_name="Data")
    notas = models.TextField(max_length=255, blank=True, verbose_name="Notas")
    realizado = models.BooleanField(
        verbose_name="Realizado?", blank=True, null=True)
    avaliacao = models.FloatField(
        verbose_name="Avaliação", blank=True, null=True)

    class Meta:
        verbose_name = "Teste"
        verbose_name_plural = "Testes"

    def __str__(self):
        return self.disciplina.descricao

# Evento


class Evento(models.Model):
    utilizador = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50, verbose_name="Título")
    descricao = models.CharField(max_length=255, verbose_name="Descrição")
    data_inicio = models.DateTimeField(verbose_name="Data de Início")
    data_fim = models.DateTimeField(verbose_name="Data de Fim")

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"

    def __str__(self):
        return self.titulo
