from django import forms
from .models import TarefaModel, Cliente, EmailModel

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nome', 'email', 'cpf', 'cnpj', )

class TarefaForm(forms.ModelForm):
    class Meta:
        model = TarefaModel

        fields = ('nome', 'mes', 'boleto',  )

class EmailForm(forms.ModelForm):
    class Meta:
        model = EmailModel
        fields = ('nome', 'email_template', )