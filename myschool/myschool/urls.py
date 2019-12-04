"""myschool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

# Views da aplicação utilizadores
from utilizadores import views as utilizadores_views

urlpatterns = [
    # Páginas Públicas
    path('', include('myschool_app.urls')),
    # Páginas da Aplicação
    path('app/', include('myschool_app.urls_app')),
    # Administração
    path('admin/docs/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    # Autenticação
    path('app/registo/', utilizadores_views.registo, name='app-registar'),
    path('app/perfil/', utilizadores_views.perfil, name="app-perfil"),
    path('app/login/', auth_views.LoginView.as_view(
        template_name='utilizadores/login.html', redirect_authenticated_user=True), name='app-login'),
    path('app/logout/', auth_views.LogoutView.as_view(), name='app-logout'),
    # Recuperação da password
    path('app/recuperar-password/', auth_views.PasswordResetView.as_view(
        template_name='utilizadores/recuperar_password.html'), name='app-recuperar-passowrd'),
    path('app/recuperar-password/concluido', auth_views.PasswordResetDoneView.as_view(
        template_name='utilizadores/recuperar_password_concluido.html'), name='app-recuperar-password-concluido'),
    path('app/recuperar-password/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='utilizadores/recuperar_password_confirmacao.html'), name='app-recuperar-password-confirmacao'),
    path('app/recuperar-password/recuperada', auth_views.PasswordResetCompleteView.as_view(
        template_name='utilizadores/recuperar_password_recuperada.html'), name='app-recuperar-password-recuperada'),
]

# Se a opção DEBUG = True
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
