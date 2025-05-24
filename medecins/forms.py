from django import forms
from .models import Medecin

class MedecinForm(forms.ModelForm):
    class Meta:
        model = Medecin
        fields = ['nom', 'prenom', 'specialite', 'telephone', 'email']
