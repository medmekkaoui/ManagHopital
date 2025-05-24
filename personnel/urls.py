from django.urls import path
from . import views
app_name = 'personnel'

urlpatterns = [
    path('secretaires/', views.liste_secretaire, name='liste_secretaire'),
    path('infirmiers/', views.liste_infirmier, name='liste_infirmier'),
    path('infirmiers/ajouter/', views.ajouter_infirmier, name='ajouter_infirmier'),
    path('infirmier/<int:infirmier_id>/', views.detail_infirmier, name='detail_infirmier'),
    path('infirmiers/<int:infirmier_id>/modifier/', views.modifier_infirmier, name='modifier_infirmier'),
    path('infirmiers/<int:infirmier_id>/supprimer/', views.supprimer_infirmier, name='supprimer_infirmier'),
]
