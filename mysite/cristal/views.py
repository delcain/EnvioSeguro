from django.shortcuts import render, redirect, get_object_or_404
from .forms import TarefaForm, ClienteForm, EmailForm
from .models import TarefaModel, Cliente, EmailModel
from PyPDF2 import PdfWriter, PdfReader
from django.views import generic
from django.conf import settings
from django.core.mail import EmailMessage
import os


def index(request):
    return render(request, 'cristal/index.html')

def email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = EmailForm()
        return render(request, 'cristal/cadastro_template.html', {'form': form})

def cliente_cadastro(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ClienteForm()
        return render(request, 'cristal/cadastro_cliente.html', {'form': form})

def cliente_lista(request):
    cliente = Cliente.objects.all()
    return render(request=request, template_name="cristal/cliente_lista.html", context={'cliente' :cliente})

def cliente_editar(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    form = ClienteForm(instance=cliente)

    if(request.method == 'POST'):
        form = ClienteForm(request.POST, instance=cliente)

        if(form.is_valid()):
            cliente.save()
            return redirect('/')
        else:
            return render(request, 'cristal/editacliente.html', {'form': form, 'cliente': cliente})
    else:
        return render(request, 'cristal/editacliente.html', {'form': form, 'cliente': cliente})



def upload(request):
    if request.method == "POST":
        form = TarefaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            encripta()
            return redirect("cristal:tarefa_listar")
    form = TarefaForm()
    tarefa = TarefaModel.objects.all()
    return render(request=request, template_name="cristal/upload.html", context={'form': form, 'tarefa': tarefa})

def encripta():
    path = "C:/apps/EnvioSeguro/mysite/media/cristal/static/cristal/"
    boleto = TarefaModel.objects.all().last()

    # inicia tratamento do path do boleto
    file = repr(boleto.boleto)
    filename = file.lstrip('<FieldFile: cristal/static/cristal/').rstrip('>')
    ok = os.path.join(path, filename)

    # Inicia tratamento do CPF
    x = repr(boleto.nome.cpf)
    cpf = x.strip('.').lstrip('CPF(raw_input=').rstrip(')')

    # Inicia Tratamento CNPJ
    z = repr(boleto.nome.cnpj)
    cnpj = z.strip('.').lstrip('CNPJ(raw_input=').rstrip(')')


    if cnpj == "''":
        senha = cpf
    else:
        senha = cnpj

    # Inicia Encriptografia do PDf
    reader = PdfReader(ok)
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    writer.encrypt(senha)
    with open(ok, "wb") as f:
        writer.write(f)

    #Inicia o envio do e-mail.

    # email_subject = 'Arquivos enviados pelo formulário'
    # email_body = 'Segue abaixo a lista dos arquivos enviados:'
    # email_to = ['diego@cuidadodigital.com.br','paulo.trindade@cuidadodigital.com.br']
    # email_from = 'suporte@cuidadodigital.com.br'
    # email = EmailMessage(email_subject, email_body, email_from, email_to)
    # email.attach_file(ok)
    # email.send()


#
# class IndexView(generic.ListView):
#     template_name = "cristal/index.html"
#     context_object_name = "ultimos_boletos_lista"
#     def get_queryset(self):
#         return TarefaModel.objects.order_by("-data_boleto")[:100]

# class DetailView(generic.DetailView):
#     template_name = "cristal/detalhes.html"
#     context_object_name = "tarefas_listar"
#     model = TarefaModel

def tarefas_listar(request):
    tarefas = TarefaModel.objects.all()
    return render(request=request, template_name="cristal/tarefa_lista.html", context={'tarefas': tarefas})