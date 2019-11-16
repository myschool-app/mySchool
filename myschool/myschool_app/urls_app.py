from django.urls import path
from .views_app import *

urlpatterns = [
    # Páginas da Aplicação
    path('', Dashboard.as_view(), name="app-inicio"),
    path('disciplinas/', DisciplinaListView.as_view(),
         name="app-disciplinas-lista"),
    path('disciplinas/adicionar/', DisciplinaFormView.as_view(),
         name="app-disciplinas-adicionar")
]
