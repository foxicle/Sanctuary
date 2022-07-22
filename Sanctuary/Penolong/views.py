from django.shortcuts import render, redirect
from Penolong.models import Hewan
from Penolong.forms import FormHewan
from django.contrib import messages

def ubah_hewan(request, id_hewan):
    hewan = Hewan.objects.get(id=id_hewan)
    template = 'ubah-hewan.html'
    if request.POST:
        form = FormHewan(request.POST, request.FILES, instance=hewan)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil Diperbaharui")
            return redirect('ubah_hewan', id_hewan=id_hewan)
    else:
        form = FormHewan(instance=hewan)
        konteks = {
            'form':form,
            'Hewan':hewan
        }
    return render(request, template, konteks)

def daftar(request):
    hewans = Hewan.objects.all()

    konteks = {
        'hewans': hewans,
    }
    return render(request,'daftar.html', konteks)


def tambah_hewan(request):
    if request.POST:
        form = FormHewan(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = FormHewan()
            pesan = "Data Berhasil Disubmit"
            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'tambah-hewan.html', konteks)
    else:
        form = FormHewan()

        konteks = {
        'form': form,
        }

    return render(request,'tambah-hewan.html',konteks)