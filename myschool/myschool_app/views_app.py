from django.contrib.auth.mixins import LoginRequiredMixin
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


class DisciplinaFormView(CreateView):
    """
    Cria uma disciplina
    """

    model = Disciplina
    template_name = 'myschool_app/app/disciplinas_form.html'
    fields = ['descricao', 'professor']
    success_url = '/app/disciplinas/'

    def form_valid(self, form):
        form.instance.utilizador = self.request.user
        return super().form_valid(form)

# Editar Disciplina


# class DisciplinaEditarView(UpdateView):
