from django.urls import path
from . import views
app_name = 'rendezvous'

urlpatterns = [
    path('', views.liste_rendezvous, name='liste_rendezvous'),
    path('ajouter/', views.ajouter_rendezvous, name='ajouter_rendezvous'),
    path('<int:id>/modifier/', views.modifier_rendezvous, name='modifier_rendezvous'),
    path('<int:id>/supprimer/', views.supprimer_rendezvous, name='supprimer_rendezvous'),
]
