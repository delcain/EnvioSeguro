from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "cristal"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detalhes"),
    path("upload/", views.upload, name="upload"),
]\
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
