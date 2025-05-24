from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Departement(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True, blank=True)
    nom = models.CharField(max_length=100)
    description = models.TextField()
    

class Equipement(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True, blank=True)
    nom = models.CharField(max_length=100)
    quantite = models.IntegerField()
    date_ajout = models.DateField(auto_now_add=True)
    