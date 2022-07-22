from tkinter import Widget
from django import forms
from django.forms import ModelForm
from Penolong.models import Hewan

class FormHewan(ModelForm):
    class Meta:
        model = Hewan
        fields = '__all__'

        widgets = {
            'Nama'      : forms.TextInput({'class':'form-control'}),
            'Deskripsi' : forms.TextInput({'class':'form-control'}),
            'Pemilik'   : forms.TextInput({'class':'form-control'}),
            'Nomor'     : forms.NumberInput({'class':'form-control'}),
            'Date'      : forms.TextInput({'class':'form-control'}),
            'Jenis_id'  : forms.Select({'class':'form-control'}),
        }