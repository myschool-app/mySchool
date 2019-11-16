from django.contrib import admin
from django.urls import path
from . import views as views_app

urlpatterns = [
    # Páginas Públicas
    path('', views_app.InicioView.as_view(), name="publico-inicio"),
    path('sobre/', views_app.SobreView.as_view(), name="publico-sobre"),
    path('funcionalidades/', views_app.FuncionalidadesViews.as_view(),
         name="publico-funcionalidades"),
    path('contactos/', views_app.ContactosView.as_view(), name="publico-contactos"),
    # Páginas da Aplicação
    path('app/', views_app.Dashboard.as_view(), name="app-inicio"),
    path('app/disciplinas/', views_app.DisciplinaListView.as_view(),
         name="app-disciplinas-lista"),
]
