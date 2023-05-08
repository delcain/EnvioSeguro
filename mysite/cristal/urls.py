from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "cristal"
urlpatterns = [
    path("", views.index, name="index"),
    path("tarefas/detalhes/int:pk>/", views.DetailView.as_view(), name="detalhes"),
    path("tarefas/upload/", views.upload, name="upload"),
    path("cliente/cadastro/", views.cliente_cadastro, name="cadastro_cliente")
]\
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
