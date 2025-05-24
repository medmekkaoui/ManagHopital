
from django.urls import path
from . import views

app_name = "facturation"
urlpatterns = [
    path('', views.liste_factures, name='liste_factures'),
    path('ajouter/', views.ajouter_facture, name='ajouter_facture'),
    path('<int:facture_id>/modifier/', views.modifier_facture, name='modifier_facture'),
    path('<int:facture_id>/supprimer/', views.supprimer_facture, name='supprimer_facture'),
]