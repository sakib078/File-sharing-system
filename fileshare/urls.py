from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.contrib.auth.models import User


urlpatterns = [
    path('', views.home, name="fileshareHome"),
    path('download/<int:file_id>/', views.download_file, name="download_file"),
    path('share/<int:file_id>/',views.share_file, name='share_file'),
    path('list/', views.shared_file_list, name='user_list'),
] + static(settings.MEDIA_URL, DOCUMENT_ROOT=settings.MEDIA_ROOT)
