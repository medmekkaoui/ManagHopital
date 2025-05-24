
from django.shortcuts import render
from .models import Departement, Equipement

def liste_departements(request):
    departements = Departement.objects.all()
    return render(request, 'administration/liste_departements.html', {'departements': departements})

def liste_equipements(request):
    equipements = Equipement.objects.all()
    return render(request, 'administration/liste_equipements.html', {'equipements': equipements})