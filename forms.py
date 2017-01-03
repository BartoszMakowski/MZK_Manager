from django import forms

from .models import Przewoznicy


class PrzewoznicyForm(forms.ModelForm):

    class Meta:
        model = Przewoznicy
        fields = ['nazwa', 'nip', 'adres'] 
