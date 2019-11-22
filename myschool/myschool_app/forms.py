from django import forms
from django.contrib.auth.models import User
from myschool_app.models import *


class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = ['descricao', 'professor', ]

    def __init__(self, *args, **kwargs):
        utilizador = kwargs.pop('user')
        super(DisciplinaForm, self).__init__(*args, **kwargs)
        self.fields['professor'].queryset = Professor.objects.filter(
            utilizador=utilizador)
