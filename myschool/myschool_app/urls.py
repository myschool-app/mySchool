from django.urls import path, include
from . import views as views_app

urlpatterns = [
    # Páginas Públicas
    path('', views_app.InicioView.as_view(), name="publico-inicio"),
    path('sobre/', views_app.SobreView.as_view(), name="publico-sobre"),
    path('equipa/', views_app.EquipaView.as_view(), name="publico-equipa"),
    path('funcionalidades/', views_app.FuncionalidadesViews.as_view(),
         name="publico-funcionalidades"),
    path('contactos/', views_app.ContactosView.as_view(), name="publico-contactos"),
]
