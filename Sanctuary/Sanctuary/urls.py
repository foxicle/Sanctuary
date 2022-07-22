from xml.dom.minidom import Document
from django.conf import settings
from django.contrib import admin
from django.urls import path
from Penolong.views import *
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', daftar,name='daftar'),
    path('tambah-hewan/',tambah_hewan,name='tambah_hewan'),
    path('hewan/ubah/<int:id_hewan>',ubah_hewan,name='ubah_hewan'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)