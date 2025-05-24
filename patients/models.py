from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Patient(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    date_naissance = models.DateField()
    adresse = models.TextField()
    telephone = models.CharField(max_length=15)
    groupe_sanguin = models.CharField(max_length=3)
     


class DossierMedical(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    antecedents = models.TextField()
    traitements = models.TextField()
    prescriptions = models.TextField()
    resultats_tests = models.TextField()