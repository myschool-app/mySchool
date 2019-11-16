from django.urls import path
from . import views as views_app

urlpatterns = [
    # Páginas da Aplicação
    path('', views_app.Dashboard.as_view(), name="app-inicio"),
    path('app/disciplinas/', views_app.DisciplinaListView.as_view(),
         name="app-disciplinas-lista"),
]
