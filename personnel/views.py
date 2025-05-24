from django.shortcuts import render, redirect, get_object_or_404
from .models import Secretaire, Infirmier
from .forms import InfirmierForm

# Ajouter un infirmier
def ajouter_infirmier(request):
    if request.method == 'POST':
        form = InfirmierForm(request.POST)
        if form.is_valid():
            infirmier = form.save()
            return redirect('personnel:liste_infirmier', )  # Redirige vers le détail
    else:
        form = InfirmierForm()
    return render(request, 'personnel/ajouter_infirmier.html', {'form': form})

# Détail d’un infirmier
def detail_infirmier(request, infirmier_id):
    infirmier = get_object_or_404(Infirmier, id=infirmier_id)
    return render(request, 'personnel/detail_infirmier.html', {'infirmier': infirmier})

def modifier_infirmier(request, infirmier_id):
    infirmier = get_object_or_404(Infirmier, id=infirmier_id)
    if request.method == 'POST':
        form = InfirmierForm(request.POST, instance=infirmier)
        if form.is_valid():
            form.save()
            return redirect('personnel:liste_infirmier')
    else:
        form = InfirmierForm(instance=infirmier)
    return render(request, 'personnel/modifier_infirmier.html', {'form': form})

def supprimer_infirmier(request, infirmier_id):
    infirmier = get_object_or_404(Infirmier, id=infirmier_id)
    if request.method == 'POST':
        infirmier.delete()
        return redirect('personnel:liste_infirmier')
    return render(request, 'personnel/supprimer_infirmier.html', {'infirmier': infirmier})

# Liste des secrétaires
def liste_secretaire(request):
    secretaires = Secretaire.objects.all()
    return render(request, 'personnel/liste_secretaire.html', {'secretaires': secretaires})

# Liste des infirmiers
def liste_infirmier(request):
    infirmiers = Infirmier.objects.all()
    return render(request, 'personnel/liste_infirmier.html', {'infirmiers': infirmiers})
