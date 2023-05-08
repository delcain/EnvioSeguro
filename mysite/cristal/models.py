import datetime
from django_cpf_cnpj.fields import CPFField, CNPJField
from django.db import models
from django.utils import timezone

class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    cpf = CPFField(masked=False, blank=True)
    cnpj = CNPJField(masked=False, blank=True)
    data_cadastro = models.DateTimeField("Data Cadastro")

    def __str__(self):
        return self.nome

class TarefaModel(models.Model):
    objects = None
    MES = (
        ('JANEIRO', 'JANEIRO'),
        ('FEVEREIRO', 'FEVEREIRO'),
        ('MARÇO', 'MARÇO'),
        ('ABRIL', 'ABRIL'),
        ('MAIO', 'MAIO'),
        ('JUNHO', 'JUNHO'),
        ('JULHO', 'JULHO'),
        ('AGOSTO', 'AGOSTO'),
        ('SETEMBRO', 'SETEMBRO'),
        ('OUTUBRO', 'OUTUBRO'),
        ('NOVEMBRO', 'NOVEMBRO'),
        ('DEZEMBRO', 'DEZEMBRO'),
    )

    mes = models.CharField(max_length=10, choices=MES, default='null')
    data_boleto = models.DateTimeField("Data Boleto", auto_now_add=True)
    nome = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    boleto = models.FileField(upload_to='cristal/static/cristal/', default='null')
    status_entrega = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return str(self.nome)