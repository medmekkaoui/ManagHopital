from django.shortcuts import render, redirect, get_object_or_404
from .models import RendezVous
from .forms import RendezVousForm

def liste_rendezvous(request):
    rendezvous = RendezVous.objects.all()
    return render(request, 'rendezvous/liste_rendezvous.html', {'rendezvous': rendezvous})

def ajouter_rendezvous(request):
    form = RendezVousForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('rendezvous/liste_rendezvous')
    return render(request, 'rendezvous/ajouter_rendezvous.html', {'form': form})

def modifier_rendezvous(request, id):
    rdv = get_object_or_404(RendezVous, id=id)
    form = RendezVousForm(request.POST or None, instance=rdv)
    if form.is_valid():
        form.save()
        return redirect('rendezvous/liste_rendezvous')
    return render(request, 'rendezvous/modifier_rendezvous.html', {'form': form})

def supprimer_rendezvous(request, id):
    rdv = get_object_or_404(RendezVous, id=id)
    if request.method == "POST":
        rdv.delete()
        return redirect('rendezvous/liste_rendezvous')
    return render(request, 'rendezvous/supprimer_rendezvous.html', {'rdv': rdv})
