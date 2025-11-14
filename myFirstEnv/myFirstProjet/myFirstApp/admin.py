from django.contrib import admin
from .models import Etudiant, Document , Filiere


class EtudiantAdmin(admin.ModelAdmin):
  list_display = ("prenom", "nom", "telephone", "adresse" , "date" , 'filiere')

class FiliereAdmin(admin.ModelAdmin):
  list_display = ('nom', 'description')
  search_fields = ('nom',)

# Register your models here.
admin.site.register(Etudiant, EtudiantAdmin)

admin.site.register(Filiere, FiliereAdmin)
admin.site.register(Document)