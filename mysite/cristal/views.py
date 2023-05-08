from django.shortcuts import render, redirect
from django.views import generic
from .models import TarefaModel
from .forms import TarefaForm
from PyPDF2 import PdfWriter, PdfReader
from django.conf import settings
from django.core.mail import EmailMessage
import os

def upload(request):
    if request.method == "POST":
        form = TarefaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            encripta()
            return redirect("cristal:upload")
    form = TarefaForm()
    tarefa = TarefaModel.objects.all()
    # boleto = TarefaModel.objects.all().last()
    # print(boleto.boleto, boleto.nome.cpf, boleto.nome.cnpj)
    return render(request=request, template_name="cristal/upload.html", context={'form': form, 'tarefa': tarefa})

def encripta():
    path = "C:/PycharmProjects/pythonProject/mysite/media/cristal/static/cristal"
    boleto = TarefaModel.objects.all().last()

    # inicia tratamento do path do boleto
    file = repr(boleto.boleto)
    filename = file.lstrip('<FieldFile: cristal/static/cristal/').rstrip('>')
    ok = os.path.join(path, filename)

    # Inicia tratamento do CPF
    x = repr(boleto.nome.cpf)
    cpf = x.strip('.').lstrip('CPF(raw_input=').rstrip(')')
    cpf2 = int(float(cpf))

    # Inicia Tratamento CNPJ
    z = repr(boleto.nome.cnpj)
    cnpj = z.strip('.').lstrip('CNPJ(raw_input=').rstrip(')')
    cnpj2 = int(float(cnpj))


    if cpf2 >= cnpj2:
        print('É Pessoa Fisica')
    else:
        print('É PJ')




    # # Inicia Encriptografia do PDf
    # reader = PdfReader(ok)
    # writer = PdfWriter()
    # for page in reader.pages:
    #     writer.add_page(page)
    # writer.encrypt(cpf)
    # with open(ok, "wb") as f:
    #     writer.write(f)

    #Inicia o envio do e-mail.

    # email_subject = 'Arquivos enviados pelo formulário'
    # email_body = 'Segue abaixo a lista dos arquivos enviados:'
    # email_to = ['diego@cuidadodigital.com.br','paulo.trindade@cuidadodigital.com.br']
    # email_from = 'suporte@cuidadodigital.com.br'
    # email = EmailMessage(email_subject, email_body, email_from, email_to)
    # email.attach_file(ok)
    # email.send()

class IndexView(generic.ListView):
    template_name = "cristal/index.html"
    context_object_name = "ultimos_boletos_lista"
    def get_queryset(self):
        return TarefaModel.objects.order_by("-data_boleto")[:100]

class DetailView(generic.DetailView):
    template_name = "cristal/detalhes.html"
    context_object_name = "ultimas_tarefas"
    model = TarefaModel