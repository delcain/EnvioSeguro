from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "cristal"
urlpatterns = [
    path("", views.index, name="index"),
    path("tarefas/", views.tarefas_listar, name='tarefa_listar'),
    #path("tarefas/detalhes/<int:pk>/", views.DetailView.as_view(), name="tarefas_listar"),
    path("tarefas/upload/", views.upload, name="upload"),

    path("clientes/", views.cliente_lista, name='clientes_listar'),
    path("cliente/cadastro/", views.cliente_cadastro, name="cadastro_cliente"),
    path("cliente/editar/<int:id>/", views.cliente_editar, name='cliente_editar'),

    path("template/", views.email, name='cadastro_template')


]\
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
