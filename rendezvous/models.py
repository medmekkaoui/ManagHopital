from django.db import models
from patients.models import Patient
from medecins.models import Medecin

class RendezVous(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medecin = models.ForeignKey(Medecin, on_delete=models.CASCADE)
    date = models.DateField()
    heure = models.TimeField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"RDV {self.patient.nom} avec Dr. {self.medecin.nom} le {self.date} à {self.heure}"
