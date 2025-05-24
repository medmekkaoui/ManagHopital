from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['nom','email','date_naissance', 'adresse', 'telephone', 'groupe_sanguin']