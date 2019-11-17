from django.urls import path
from .views_app import *

urlpatterns = [
    # Páginas da Aplicação
    path('', Dashboard.as_view(), name="app-inicio"),
    path('disciplinas/', DisciplinaListView.as_view(),
         name="app-disciplinas-lista"),
    path('disciplinas/adicionar/', DisciplinaCreateView.as_view(),
         name="app-disciplinas-adicionar"),
    path('disciplinas/<int:pk>/editar/',
         DisciplinaUpdateView.as_view(), name="app-disciplinas-editar"),
    path('disciplinas/<int:pk>/remover/',
         DisciplinaDeleteView.as_view(), name="app-disciplinas-remover")
]
