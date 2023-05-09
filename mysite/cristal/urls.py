from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "cristal"
urlpatterns = [
    path("", views.index, name="index"),
    path("home", views.index, name="index"),
    path("tarefas/", views.tarefas_listar, name='tarefas_listar'),
    path("tarefas/upload/", views.tarefas_novo, name="tarefas_novo"),


    path("clientes/", views.cliente_lista, name='clientes_listar'),
    path("cliente/cadastro/", views.cliente_cadastro, name="cadastro_cliente"),
    path("cliente/editar/<int:id>/", views.cliente_editar, name='cliente_editar'),

    path("template/", views.template_mail_listar, name='template_listar'),
    path("template/novo", views.template_email_novo, name='template_novo'),
    path("template/editar/<int:id>/", views.template_email_editar, name='template_editar'),


]\
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
