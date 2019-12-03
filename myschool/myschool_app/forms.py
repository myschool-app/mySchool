from django import forms
from django.contrib.auth.models import User
from myschool_app.models import *
import datetime

# Disciplinas


class DisciplinaForm(forms.ModelForm):
    """
    Formulário para criação e edição de disciplinas
    """

    class Meta:
        model = Disciplina
        fields = ['descricao', 'professor', ]

    def __init__(self, *args, **kwargs):
        # utilizador que tem sessão iniciada na aplicação
        utilizador = kwargs.pop('user')
        super(DisciplinaForm, self).__init__(*args, **kwargs)
        # filtra os professores que pertencem ao utilizador acima
        self.fields['professor'].queryset = Professor.objects.filter(
            utilizador=utilizador)

# Testes


class TesteForm(forms.ModelForm):
    """
    Formulário para criação e edição de testes
    """

    class Meta:
        model = Teste
        fields = ['disciplina', 'data', 'notas']

    def __init__(self, *args, **kwargs):
        # utilizador que tem sessão iniciada na aplicação
        utilizador = kwargs.pop('user')
        super(TesteForm, self).__init__(*args, **kwargs)
        # filtra os professores que pertencem ao utilizador acima
        self.fields['disciplina'].queryset = Disciplina.objects.filter(
            utilizador=utilizador)

    """
    Verifica se a data introduzida pelo utilizador não é no passado.
    Caso seja, informa o utilizador com uma mensagem de erro.
    """

    def clean_data(self):
        data = self.cleaned_data['data']
        if data < datetime.date.today():
            raise forms.ValidationError("A data não pode ser no passado")
        return data


# Testes


class TesteAvaliacaoForm(forms.ModelForm):
    """
    Formulário para criação e edição de testes
    """

    class Meta:
        model = Teste
        fields = ['realizado', 'avaliacao', 'notas']
