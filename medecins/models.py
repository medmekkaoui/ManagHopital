from django.db import models
from django.contrib.auth.models import User
from patients.models import Patient
from django.conf import settings

from django.db import models

class Medecin(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    specialite = models.CharField(max_length=100)
    telephone = models.CharField(max_length=15)
    email = models.EmailField()
    class Meta:
        db_table = 'medecins_medecin'

    def __str__(self):
        return f"{self.nom} {self.prenom}"


class Prescription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True, blank=True)
    medecin = models.ForeignKey(Medecin, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    contenu = models.TextField()
    date = models.DateField(auto_now_add=True)