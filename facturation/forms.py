from django import forms
from .models import Facture

class FactureForm(forms.ModelForm):
    class Meta:
        model = Facture
        fields = ['patient', 'rendezvous', 'montant', 'description', 'est_payee']
