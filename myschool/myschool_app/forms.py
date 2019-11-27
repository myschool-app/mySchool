from django import forms
from django.contrib.auth.models import User
from myschool_app.models import *


class DisciplinaForm(forms.ModelForm):
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
