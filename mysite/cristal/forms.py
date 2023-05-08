from django import forms
from .models import TarefaModel, Cliente

class TarefaForm(forms.ModelForm):
    class Meta:
        model = TarefaModel
        fields = ('nome', 'mes', 'boleto', )

class CadastroClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nome', 'email', 'cpf', 'cnpj',)