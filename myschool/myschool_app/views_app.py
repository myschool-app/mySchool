from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView
)
from .models import *


# Dashboard


class Dashboard(LoginRequiredMixin, TemplateView):
    """
    Mostra a página inicial da aplicação
    """
    template_name = 'myschool_app/app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Contagem das disciplinas
        context['quantidade_disciplinas'] = Disciplina.objects.filter(
            utilizador=self.request.user).count()
        # Contagem dos professores
        context['quantidade_professores'] = Professor.objects.filter(
            utilizador=self.request.user).count()
        return context

# Lista de Disciplinas


class DisciplinaListView(LoginRequiredMixin, ListView):
    """
    Mostra a lista de disciplinas
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

    model = Disciplina
    template_name = 'myschool_app/app/disciplinas_form.html'
    fields = ['descricao', 'professor']
    success_url = reverse_lazy('app-disciplinas-lista')
    success_message = "A disciplina %(descricao)s foi criada com sucesso!"

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
    fields = ['descricao', 'professor']
    success_url = reverse_lazy('app-disciplinas-lista')
    context_object_name = 'disciplina'
    success_message = "A disciplina %(descricao)s foi atualizada com sucesso!"

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
