from django.urls import path
from . import views

app_name = 'patients'

urlpatterns = [
    path('patients/', views.liste_patients, name='liste_patients'),
    path('patients/ajouter/', views.ajouter_patients, name='ajouter_patients'),  # URL pour ajouter un patient
    path('patients/<int:patient_id>/', views.detail_patient, name='detail_patient'),
    path('<int:patient_id>/modifier/', views.modifier_patients, name='modifier_patients'),
    path('<int:patient_id>/supprimer/', views.supprimer_patients, name='supprimer_patients'),

]
