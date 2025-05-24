from django.db import models
from rendezvous.models import RendezVous
from patients.models import Patient  # adapte le chemin selon ton app

class Facture(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    rendezvous = models.OneToOneField(RendezVous, on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    est_payee = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Facture pour {self.patient.nom} le {self.date}"
