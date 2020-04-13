from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import *


# Disciplina


class TesteInline(admin.TabularInline):
    model = Teste


@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    inlines = [
        TesteInline,
    ]
    list_display = ['utilizador', 'descricao', 'professor']
    search_fields = ['utilizador__username', 'professor__nome']
    list_filter = ['utilizador', 'professor']


# Professor
class DisciplinaInline(admin.TabularInline):
    model = Disciplina


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    inlines = [
        DisciplinaInline,
    ]
    list_display = ['utilizador', 'nome', 'email']
    list_filter = ['utilizador']


# Teste
@admin.register(Teste)
class TesteAdmin(admin.ModelAdmin):
    list_display = ['utilizador', 'disciplina', 'data']
    list_filter = ['utilizador']


# Evento
@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ['utilizador', 'titulo', 'descricao']
    list_filter = ['utilizador']


# Personalização da área de administração
admin.site.site_header = 'mySchool'
admin.site.site_title = 'mySchool'
admin.site.index_title = _('Administração da aplicação mySchool')
