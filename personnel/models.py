from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Secretaire(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    telephone = models.CharField(max_length=15)

class Infirmier(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.prenom} {self.nom}"
