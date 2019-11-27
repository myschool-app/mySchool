from django.urls import path
from .views_app import *

urlpatterns = [
    # Dashboard
    path('', Dashboard.as_view(), name="app-inicio"),
    # Disciplinas
    path('disciplinas/', DisciplinaListView.as_view(),
         name="app-disciplinas-lista"),
    path('disciplinas/adicionar/', DisciplinaCreateView.as_view(),
         name="app-disciplinas-adicionar"),
    path('disciplinas/<int:pk>/editar/',
         DisciplinaUpdateView.as_view(), name="app-disciplinas-editar"),
    path('disciplinas/<int:pk>/remover/',
         DisciplinaDeleteView.as_view(), name="app-disciplinas-remover"),
    # Professores
    path('professores/', ProfessorListView.as_view(),
         name="app-professores-lista"),
    path('professores/adicionar/', ProfessorCreateView.as_view(),
         name="app-professores-adicionar"),
    path('professores/<int:pk>/editar/',
         ProfessorUpdateView.as_view(), name="app-professores-editar"),
    path('professores/<int:pk>/remover/',
         ProfessorDeleteView.as_view(), name="app-professores-remover")
]
