from django.urls import path
from . import views

urlpatterns = [
    path('departements/', views.liste_departements, name='liste_departements'),
    path('equipements/', views.liste_equipements, name='liste_equipements'),
]
