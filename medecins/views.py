from django.shortcuts import render
from .models import Medecin, Prescription
from .forms import MedecinForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

def detail_medecins(request, pk):
    medecin = get_object_or_404(Medecin, pk=pk)
    return render(request, 'medecins/detail_medecins.html', {'medecins': medecin})


def liste_medecins(request):
    medecins = Medecin.objects.all()
    return render(request, 'medecins/liste_medecins.html', {'medecins': medecins})
# Ajouter un médecin
def ajouter_medecins(request):
    if request.method == 'POST':
        form = MedecinForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medecins:liste_medecins')
    else:
        form = MedecinForm()
    return render(request, 'medecins/ajouter_medecins.html', {'form': form})

# Modifier un médecin
def modifier_medecin(request, pk):
    medecin = get_object_or_404(Medecin, pk=pk)
    if request.method == 'POST':
        form = MedecinForm(request.POST, instance=medecin)
        if form.is_valid():
            form.save()
            return redirect('medecins:liste_medecins')
    else:
        form = MedecinForm(instance=medecin)
    return render(request, 'medecins/modifier_medecin.html', {'form': form})

# Supprimer un médecin
def supprimer_medecin(request, pk):
    medecin = get_object_or_404(Medecin, pk=pk)
    if request.method == 'POST':
        medecin.delete()
        return redirect('medecins:liste_medecins')
    return render(request, 'medecins/supprimer_medecin.html', {'medecin': medecin})