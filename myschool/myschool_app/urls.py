from django.urls import path

from .views import *

urlpatterns = [
    # Páginas Públicas
    path('', InicioView.as_view(), name="publico-inicio"),
    path('sobre/', SobreView.as_view(), name="publico-sobre"),
    path('equipa/', EquipaView.as_view(), name="publico-equipa"),
    path('funcionalidades/', FuncionalidadesViews.as_view(),
         name="publico-funcionalidades"),
    path('contactos/', ContactosView.as_view(), name="publico-contactos")
]
