from django.shortcuts import render, redirect,get_object_or_404

from .models import Patient, DossierMedical
from .forms import PatientForm

def ajouter_patients(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()  # Sauvegarde le patient dans la base de données
            return redirect('patients:liste_patients')  # Redirige vers la liste des patients après ajout
    else:
        form = PatientForm()  # Crée un formulaire vide pour GET

    return render(request, 'patients/ajouter_patients.html', {'form': form})


def liste_patients(request):
    patients = Patient.objects.all()
    return render(request, 'patients/liste_patients.html', {'patients': patients})

def detail_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    dossier = DossierMedical.objects.filter(patient=patient).first()
    return render(request, 'patients/detail_patient.html', {'patient': patient, 'dossier': dossier})
def modifier_patients(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patients:liste_patients')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'patients/modifier_patients.html', {'form': form})

def supprimer_patients(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    if request.method == 'POST':
        patient.delete()
        return redirect('patients:liste_patients')
    return render(request, 'patients/confirmer_suppression.html', {'patient': patient})