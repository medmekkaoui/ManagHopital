from django import forms
from .models import Infirmier

class InfirmierForm(forms.ModelForm):
    class Meta:
        model = Infirmier
        fields = ['nom', 'prenom', 'email', 'telephone']  # Ajoute les champs nécessaires pour l'infirmier
