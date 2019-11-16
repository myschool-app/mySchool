from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView
)
from .models import *


"""
Páginas Públicas
"""

# Página Inicial


class InicioView(TemplateView):
    """
    Mostra a página inicial
    """
    template_name = 'myschool_app/publico/index.html'

# Funcionalidades


class FuncionalidadesViews(TemplateView):
    """
    Mostra a página funcionalidades
    """
    template_name = 'myschool_app/publico/funcionalidades.html'

# Sobre


class SobreView(TemplateView):
    """
    Mostra a página sobre
    """
    template_name = 'myschool_app/publico/sobre.html'

# Contactos


class ContactosView(TemplateView):
    """
    Mostra a página contactos
    """
    template_name = 'myschool_app/publico/contactos.html'


"""
Aplicação
"""

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
