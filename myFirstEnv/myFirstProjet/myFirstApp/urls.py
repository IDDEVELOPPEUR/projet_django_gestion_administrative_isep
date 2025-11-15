from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include

from django.contrib.auth import views as auth_views

urlpatterns = [

    path('myFirstApp/', views.apprenants, name='etudiantsd'),
    #path('myFirstApp/details/<int:id>', views.details, name='details'),
    path('home/', views.home, name='home'),
    path('inscription/',views.inscription, name='inscription'),
    path('accounts/login/',views.connexion, name='login'),
    path('dossier/', views.dossier, name='dossier'),
    path('accounts/logout/', views.logout, name='logout'),
    path('profile/', views.profil_utilisateur, name='profil_utilisateur'),
    path('connected/', views.home_connecte, name='home_connect'),


    path('', views.home_principal, name='home_principal'),
    path('administration/', views.administration, name='administration'),
    path('administration/filieres', views.listeFilieres, name='listeFilieres'),
    path('administration/filieres/ajouter/', views.ajouter_filiere, name='ajouter_filiere'),
    path('administration/filieres/<int:filiere_id>/etudiants', views.etudiants, name='etudiants'),
    path('administration/filieres/etudiants/details/<int:id>', views.details, name='details'),
    path('etudiants/ajouter/<int:filiere_id>/', views.ajouter_etudiant, name='ajouter_etudiant'),
    path('etudiants/supprimer/<int:id>/', views.supprimer_etudiant, name='supprimer_etudiant'),

    path('page_recupcours/', views.page_recupcours, name='page_recupcours'),
    path('upload/', views.upload_cours, name='upload_cours'),
    path('success/', views.success_page, name='success_page'), # Example success page


    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name='reset_password'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_send.html"), name='reset_password_sent'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), name='password_reset_form'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), name='password_reset_done'),
]


