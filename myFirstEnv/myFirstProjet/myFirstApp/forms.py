from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Etudiant, Document , Filiere
from django.contrib.auth.forms import PasswordResetForm

class FormulaireInscription(UserCreationForm):
    class Meta():
        model = User 
        fields = ('username','email','password1','password2')

class EtudiantForm(ModelForm):
    class Meta:
        model = Etudiant
        fields = '__all__'
        exclude = ['utilisateur']

class AdminEtudiantForm(ModelForm):
    class Meta:
        model = Etudiant
        fields = ['pdf_file']

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'pdf_file']

class FiliereForm(forms.ModelForm):
    class Meta:
        model = Filiere
        fields = ['nom', 'description']