from django.contrib import admin
from Penolong.models import Hewan, Jenis
# Register your models here.

class HewanAdmin(admin.ModelAdmin):
    list_display = ['Nama','Deskripsi','Pemilik','Date','Nomor']
    search_fields = ['Nama','Pemilik']
    list_filter = ('Jenis_id',)
    list_per_page: 10

admin.site.register(Hewan, HewanAdmin)
admin.site.register(Jenis)
