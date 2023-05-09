from django.shortcuts import render, redirect, get_object_or_404
from .forms import TarefaForm, ClienteForm, EmailForm
from .models import TarefaModel, Cliente, EmailModel
from PyPDF2 import PdfWriter, PdfReader
from django.views import generic
from django.conf import settings
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
import os

@login_required
def index(request):
    return render(request, 'cristal/index.html')

@login_required

def template_email_novo(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = EmailForm()
        return render(request, 'cristal/cadastro_template.html', {'form': form})

@login_required

def template_mail_listar(request):
    form = EmailModel.objects.all()
    return render(request=request, template_name="cristal/template_lista.html", context={'form': form})

@login_required

def template_email_editar(request, id):
    template = get_object_or_404(EmailModel, pk=id)
    form = EmailForm(instance=template)
    if(request.method == 'POST'):
        form = EmailForm(request.POST, instance=template)
        if(form.is_valid()):
            template.save()
            return redirect('/')
        else:
            return render(request, 'cristal/template_mail_editar.html', {'form': form, 'template': template})
    else:
        return render(request, 'cristal/template_mail_editar.html', {'form': form,'template':template})

@login_required

def cliente_cadastro(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ClienteForm()
        return render(request, 'cristal/cadastro_cliente.html', {'form': form})

@login_required

def cliente_lista(request):
    cliente = Cliente.objects.all()
    return render(request=request, template_name="cristal/cliente_lista.html", context={'cliente' :cliente})

@login_required

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

@login_required

def tarefas_listar(request):
    tarefas = TarefaModel.objects.all()
    return render(request=request, template_name="cristal/tarefa_lista.html", context={'tarefas': tarefas})

@login_required

def tarefas_novo(request):
    if request.method == "POST":
        form = TarefaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            encripta()
            return redirect("cristal:index")
    form = TarefaForm()
    return render(request=request, template_name="cristal/tarefa_upload.html", context={'form': form})

@login_required

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


    subject, from_email, to = "Tarefa Cadastrada com Sucesso", "suporte@cuidadodigital.com.br", "diego@cuidadodigital.com.br"
    text_content = "Tarefa Cadastrada com Sucesso"
    html_content = boleto.email_template.email_template
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.attach_file(ok)
    msg.send()