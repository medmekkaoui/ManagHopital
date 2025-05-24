from django.shortcuts import render, get_object_or_404, redirect
from .models import Facture
from .forms import FactureForm

def liste_factures(request):
    factures = Facture.objects.all()
    return render(request, 'facturation/liste_factures.html', {'factures': factures})

def ajouter_facture(request):
    if request.method == 'POST':
        form = FactureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('facturation:liste_factures')
    else:
        form = FactureForm()
    return render(request, 'facturation/ajouter_facture.html', {'form': form})

def modifier_facture(request, facture_id):
    facture = get_object_or_404(Facture, id=facture_id)
    if request.method == 'POST':
        form = FactureForm(request.POST, instance=facture)
        if form.is_valid():
            form.save()
            return redirect('facturation:liste_factures')
    else:
        form = FactureForm(instance=facture)
    return render(request, 'facturation:modifier_facture.html', {'form': form})

def supprimer_facture(request, facture_id):
    facture = get_object_or_404(Facture, id=facture_id)
    if request.method == 'POST':
        facture.delete()
        return redirect('liste_factures')
    return render(request, 'facturation:supprimer_facture.html', {'facture': facture})

