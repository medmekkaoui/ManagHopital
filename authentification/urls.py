from django.urls import path
from . import views
from django.shortcuts import render


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('', lambda request: render(request, 'authentification/dashboard.html'), name='dashboard'),
]
