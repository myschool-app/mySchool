from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (
  ListView,
  CreateView,
  UpdateView,
  DeleteView,
  TemplateView
)

from .forms import *
from .models import *

"""
Dashboard
"""


class Dashboard(LoginRequiredMixin, TemplateView):
  """
  Mostra a página inicial da aplicação
  """
  template_name = 'myschool_app/app/index.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    """
    Contagem de objetos nas diferentes secções
    """
    context['quantidade_disciplinas'] = Disciplina.objects.filter(
      utilizador=self.request.user).count()
    context['quantidade_professores'] = Professor.objects.filter(
      utilizador=self.request.user).count()
    context['quantidade_testes'] = Teste.objects.filter(
      utilizador=self.request.user).count()
    context['quantidade_eventos'] = Evento.objects.filter(
      utilizador=self.request.user).count()

    context['testes'] = Teste.objects.filter(utilizador=self.request.user)
    context['eventos'] = Evento.objects.filter(
      utilizador=self.request.user)

    return context


"""
Disciplinas
"""


# Lista de disciplinas


class DisciplinaListView(LoginRequiredMixin, ListView):
  """
  Mostra a lista de disciplinas, próprias de cada utilizador
  registado na tabela Disciplina
  """

  model = Disciplina
  template_name = 'myschool_app/app/disciplinas.html'
  context_object_name = 'disciplinas'

  def get_queryset(self):
    return Disciplina.objects.filter(utilizador=self.request.user)


# Adicionar Disciplina


class DisciplinaCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
  """
  Cria uma disciplina
  """

  template_name = 'myschool_app/app/disciplinas_form.html'
  form_class = DisciplinaForm
  success_url = reverse_lazy('app-disciplinas-lista')
  success_message = "A disciplina %(descricao)s foi criada com sucesso!"

  def get_form_kwargs(self):
    kwargs = super(DisciplinaCreateView, self).get_form_kwargs()
    kwargs['user'] = self.request.user
    return kwargs

  def form_valid(self, form):
    form.instance.utilizador = self.request.user
    return super().form_valid(form)


# Editar Disciplina


class DisciplinaUpdateView(LoginRequiredMixin, SuccessMessageMixin, UserPassesTestMixin, UpdateView):
  """
  Edita uma disciplina
  """

  model = Disciplina
  template_name = 'myschool_app/app/disciplinas_form.html'
  form_class = DisciplinaForm
  success_url = reverse_lazy('app-disciplinas-lista')
  context_object_name = 'disciplina'
  success_message = "A disciplina %(descricao)s foi atualizada com sucesso!"

  def get_form_kwargs(self):
    kwargs = super(DisciplinaUpdateView, self).get_form_kwargs()
    kwargs['user'] = self.request.user
    return kwargs

  def form_valid(self, form):
    form.instance.utilizador = self.request.user
    return super().form_valid(form)

  def test_func(self):
    disciplina = self.get_object()
    if self.request.user == disciplina.utilizador:
      return True
    return False


# Remover Disciplina


class DisciplinaDeleteView(LoginRequiredMixin, SuccessMessageMixin, UserPassesTestMixin, DeleteView):
  """
  Remove uma disciplina
  """

  model = Disciplina
  template_name = 'myschool_app/app/disciplinas_remover.html'
  success_url = reverse_lazy('app-disciplinas-lista')
  context_object_name = 'disciplina'
  success_message = "A disciplina %(descricao)s foi removida com sucesso!"

  def test_func(self):
    disciplina = self.get_object()
    if self.request.user == disciplina.utilizador:
      return True
    return False

  def delete(self, request, *args, **kwargs):
    disciplina = self.get_object()
    messages.success(self.request, self.success_message %
                     disciplina.__dict__)
    return super(DisciplinaDeleteView, self).delete(request, *args, **kwargs)


"""
Professores
"""


# Lista de Professores


class ProfessorListView(LoginRequiredMixin, ListView):
  """
  Mostra a lista de professores, próprios de cada utilizador
  registado na tabela Professor
  """

  model = Professor
  template_name = 'myschool_app/app/professores.html'
  context_object_name = 'professores'

  def get_queryset(self):
    return Professor.objects.filter(utilizador=self.request.user)


# Adicionar Professor


class ProfessorCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
  """
  Cria uma professor
  """

  model = Professor
  fields = ['nome', 'email', 'telefone']
  template_name = 'myschool_app/app/professores_form.html'
  success_url = reverse_lazy('app-professores-lista')
  success_message = "O professor %(nome)s foi adicionado com sucesso!"

  def form_valid(self, form):
    form.instance.utilizador = self.request.user
    return super().form_valid(form)


# Editar Professor


class ProfessorUpdateView(LoginRequiredMixin, SuccessMessageMixin, UserPassesTestMixin, UpdateView):
  """
  Edita uma disciplina
  """

  model = Professor
  template_name = 'myschool_app/app/professores_form.html'
  fields = ['nome', 'email', 'telefone']
  success_url = reverse_lazy('app-professores-lista')
  context_object_name = 'professor'
  success_message = "O professor %(nome)s foi atualizado com sucesso!"

  def form_valid(self, form):
    form.instance.utilizador = self.request.user
    return super().form_valid(form)

  def test_func(self):
    professor = self.get_object()
    if self.request.user == professor.utilizador:
      return True
    return False


# Remover Professor


class ProfessorDeleteView(LoginRequiredMixin, SuccessMessageMixin, UserPassesTestMixin, DeleteView):
  """
  Remove um professor
  """

  model = Professor
  template_name = 'myschool_app/app/professores_remover.html'
  success_url = reverse_lazy('app-professores-lista')
  context_object_name = 'professor'
  success_message = "O professor %(nome)s foi removido com sucesso!"

  def test_func(self):
    professor = self.get_object()
    if self.request.user == professor.utilizador:
      return True
    return False

  def delete(self, request, *args, **kwargs):
    professor = self.get_object()
    messages.success(self.request, self.success_message %
                     professor.__dict__)
    return super(ProfessorDeleteView, self).delete(request, *args, **kwargs)


"""
Testes
"""


# Lista de Testes


class TesteListView(LoginRequiredMixin, ListView):
  """
  Mostra a lista de testes, próprios de cada utilizador
  registado na tabela Teste
  """

  model = Teste
  template_name = 'myschool_app/app/testes.html'
  context_object_name = 'testes'

  def get_queryset(self):
    return Teste.objects.filter(utilizador=self.request.user)


# Adicionar Teste


class TesteCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
  """
  Cria um teste
  """

  template_name = 'myschool_app/app/testes_form.html'
  form_class = TesteForm
  success_url = reverse_lazy('app-testes-lista')
  success_message = "O teste da disciplina %(disciplina)s foi criado com sucesso!"

  def get_form_kwargs(self):
    kwargs = super(TesteCreateView, self).get_form_kwargs()
    kwargs['user'] = self.request.user
    return kwargs

  def form_valid(self, form):
    form.instance.utilizador = self.request.user
    return super().form_valid(form)


# Editar Teste


class TesteUpdateView(LoginRequiredMixin, SuccessMessageMixin, UserPassesTestMixin, UpdateView):
  """
  Edita um teste
  """

  model = Teste
  template_name = 'myschool_app/app/testes_form.html'
  form_class = TesteForm
  success_url = reverse_lazy('app-testes-lista')
  success_message = "O teste da disciplina %(disciplina)s foi atualizado com sucesso!"

  def get_form_kwargs(self):
    kwargs = super(TesteUpdateView, self).get_form_kwargs()
    kwargs['user'] = self.request.user
    return kwargs

  def form_valid(self, form):
    form.instance.utilizador = self.request.user
    return super().form_valid(form)

  def test_func(self):
    teste = self.get_object()
    if self.request.user == teste.utilizador:
      return True
    return False


# Adicionar Avaliação a Teste


class TesteAvaliacaoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UserPassesTestMixin, UpdateView):
  """
  Adiciona a avaliação a um teste
  """

  model = Teste
  template_name = 'myschool_app/app/testes_avaliacao_form.html'
  form_class = TesteAvaliacaoForm
  success_url = reverse_lazy('app-testes-lista')
  success_message = "Foi adicionada a avaliação de %(avaliacao)s ao teste!"

  def form_valid(self, form, **kwargs):
    """
    Preenchimentos dos campos após o utilizador guardar o formulário
    """

    form.instance.utilizador = self.request.user
    form.instance.realizado = True
    return super().form_valid(form)

  def test_func(self):
    teste = self.get_object()
    if self.request.user == teste.utilizador:
      return True
    return False


# Remover Teste


class TesteDeleteView(LoginRequiredMixin, SuccessMessageMixin, UserPassesTestMixin, DeleteView):
  """
  Remove um teste
  """

  model = Teste
  template_name = 'myschool_app/app/testes_remover.html'
  success_url = reverse_lazy('app-testes-lista')
  context_object_name = 'teste'
  success_message = "O teste do dia %(data)s foi removido com sucesso!"

  def test_func(self):
    teste = self.get_object()
    if self.request.user == teste.utilizador:
      return True
    return False

  def delete(self, request, *args, **kwargs):
    teste = self.get_object()
    messages.success(self.request, self.success_message % teste.__dict__)
    return super(TesteDeleteView, self).delete(request, *args, **kwargs)


"""
Eventos
"""


# Lista de Eventos


class EventoListView(LoginRequiredMixin, ListView):
  """
  Mostra a lista de eventos, próprios de cada utilizador
  registado na tabela Evento
  """

  model = Evento
  template_name = 'myschool_app/app/eventos.html'
  context_object_name = 'eventos'

  def get_queryset(self):
    return Evento.objects.filter(utilizador=self.request.user)


# Adicionar Evento


class EventoCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
  """
  Cria um evento
  """

  model = Evento
  fields = ['titulo', 'descricao', 'data_inicio', 'data_fim']
  template_name = 'myschool_app/app/eventos_form.html'
  success_url = reverse_lazy('app-eventos-lista')
  success_message = "O evento com o título %(titulo)s foi criado com sucesso!"

  def form_valid(self, form):
    form.instance.utilizador = self.request.user
    return super().form_valid(form)


# Editar Evento


class EventoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UserPassesTestMixin, UpdateView):
  """
  Edita um evento
  """

  model = Evento
  fields = ['titulo', 'descricao', 'data_inicio', 'data_fim']
  template_name = 'myschool_app/app/eventos_form.html'
  success_url = reverse_lazy('app-eventos-lista')
  success_message = "O evento com o título %(titulo)s foi atualizado com sucesso!"

  def form_valid(self, form):
    form.instance.utilizador = self.request.user
    return super().form_valid(form)

  def test_func(self):
    evento = self.get_object()
    if self.request.user == evento.utilizador:
      return True
    return False


# Remover Evento


class EventoDeleteView(LoginRequiredMixin, SuccessMessageMixin, UserPassesTestMixin, DeleteView):
  """
  Remove um evento
  """

  model = Evento
  template_name = 'myschool_app/app/eventos_remover.html'
  success_url = reverse_lazy('app-eventos-lista')
  context_object_name = 'evento'
  success_message = "O evento com o título %(titulo)s foi removido com sucesso!"

  def test_func(self):
    evento = self.get_object()
    if self.request.user == evento.utilizador:
      return True
    return False

  def delete(self, request, *args, **kwargs):
    evento = self.get_object()
    messages.success(self.request, self.success_message % evento.__dict__)
    return super(EventoDeleteView, self).delete(request, *args, **kwargs)


"""
Gráficos
"""
