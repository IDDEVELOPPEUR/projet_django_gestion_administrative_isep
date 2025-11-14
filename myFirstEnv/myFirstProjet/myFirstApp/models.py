from django.db import models
from django.contrib.auth.models import User
from django.forms import ImageField
from django.contrib import admin


class Etudiant(models.Model):
  utilisateur= models.OneToOneField(User, null=True, on_delete=models.CASCADE)
  prenom = models.CharField(max_length=255)
  nom = models.CharField(max_length=255)
  telephone=models.IntegerField(null=True)
  adresse=models.CharField(max_length=229)
  date=models.DateField(null=True)
  filiere = models.ForeignKey('Filiere', null=True ,on_delete=models.CASCADE, related_name='etudiants')
  imageProfil=models.ImageField(null=True, default="fatou.jpg", blank=True)
  pdf_file = models.FileField(null=True, upload_to='documents/pdfs/')

  def _str_(self):
    return f"{self.prenom} {self.nom}"


class Document(models.Model):
  #filiere = models.CharField(max_length=255)
  title = models.CharField(max_length=255)
  pdf_file = models.FileField(upload_to='documents/pdfs/')

  def __str__(self):
    return self.title

class Filiere(models.Model):
  nom = models.CharField(max_length=100, unique=True)
  description = models.TextField(blank=True)

  def __str__(self):
    return self.nom
