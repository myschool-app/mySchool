from django.views.generic import TemplateView

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


class EquipaView(TemplateView):
    """
    Mostra a página equipa
    """
    template_name = 'myschool_app/publico/equipa.html'

# Contactos


class ContactosView(TemplateView):
    """
    Mostra a página contactos
    """
    template_name = 'myschool_app/publico/contactos.html'
