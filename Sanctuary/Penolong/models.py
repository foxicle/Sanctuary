from sqlite3 import Date
from django.db import models
import os

# Create your models here.

def get_file_path_foto( instance, filename):
    ext = os.path.splitext(filename)[1]
    filename = "%s%s" % (instance.nip, ext)
    return os.path.join('images/', filename)

class Jenis(models.Model):
    jenis = models.CharField(max_length=20)

    def __str__(self):
        return self.jenis

class Hewan(models.Model):
    Nama        = models.CharField(max_length=90)
    Deskripsi   = models.TextField(null=True)
    Pemilik     = models.CharField(max_length=90)
    Nomor       = models.IntegerField()
    Date        = models.DateTimeField()
    Jenis_id    = models.ForeignKey(Jenis,on_delete=models.CASCADE,null=True)
    gambar      = models.ImageField(upload_to='gambar', null=True)

    def __str__(self):
        return self.Nama

