from django.urls import path
from . import views
app_name = "medecins"
urlpatterns = [
    path('medecins/', views.liste_medecins, name='liste_medecins', ),
    path('ajouter', views.ajouter_medecins, name='ajouter_medecins'),
    path('<int:pk>/', views.detail_medecins, name='detail_medecins'),
    path('<int:pk>/modifier', views.modifier_medecin, name='modifier_medecin'),
    path('<int:pk>/supprimer', views.supprimer_medecin, name='supprimer_medecin'),
]
