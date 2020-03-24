from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UtilizadorRegistoForm(UserCreationForm):
  """
  Formulário para registo de novos utilizadores
  """

  first_name = forms.CharField(required=True, label="Primeiro Nome")
  last_name = forms.CharField(required=True, label="Último Nome")
  email = forms.EmailField()

  class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name',
              'email', 'password1', 'password2']


class UtilizadorUpdateForm(forms.ModelForm):
  """
  Formulário para atualização dos dados de cada utilizador,
  como Primeiro e Último Nome e Email.
  """

  first_name = forms.CharField(required=True)
  last_name = forms.CharField(required=True)
  email = forms.EmailField()

  class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
