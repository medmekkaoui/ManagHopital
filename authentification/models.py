from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class CustomUser(AbstractUser):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True, blank=True)
    ROLES = [
        ('patient', 'Patient'),
        ('medecin', 'Médecin'),
        ('secretaire', 'Secrétaire'),
        ('infirmier', 'Infirmier'),
        ('admin', 'Administrateur'),
    ]
    role = models.CharField(max_length=20, choices=ROLES, default='patient')

    def __str__(self):
        return f"{self.username} ({self.role})"
