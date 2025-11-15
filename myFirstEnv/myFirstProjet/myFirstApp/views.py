from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import Group
from .models import Etudiant, Document , Filiere
from .forms import FormulaireInscription, AdminEtudiantForm , FiliereForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from .forms import EtudiantForm, DocumentForm
from .decorators import authenticated
from django.shortcuts import get_object_or_404




def inscription(request):
    form = FormulaireInscription()

    if request.method == 'POST':
        form = FormulaireInscription(request.POST)
        if form.is_valid():
            new_user = form.save()
            #message de succès
            messages.success(request, f"Le compte a été créé pour {new_user.username}.")
            groupe = Group.objects.get(name="Etudiant")
            new_user.groups.add(groupe)

            auth_login(request, new_user)
            return redirect('profil_utilisateur')

    return render(request, 'inscription.html', {'formulaire': form})



def apprenants(request):
    etudiants = Etudiant.objects.all().values()
    template = loader.get_template('etudiants.html')
    context = {
    'etudiants': etudiants
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    etudiants = Etudiant.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
    'etudiants': etudiants,
    }
    return HttpResponse(template.render(context, request))


def home_principal(request):

    return render(request, 'home.html')




@login_required
def home_connecte(request):
    user = request.user

    # Ici je force la création du profil
    if not hasattr(user, 'etudiant'):
        messages.info(request, "Veuillez compléter votre profil pour continuer.")
        return redirect('profil_utilisateur')

    context = {
        "is_admin": user.groups.filter(name='Admin').exists() or user.is_staff,
        "is_etudiant": user.groups.filter(name='Etudiant').exists(),
        "is_responsable": user.groups.filter(name='Responsable').exists(),
    }

    return render(request, 'home_connect.html', context)


def home(request):
    return render(request, 'home.html')


def template(request):
  mesdonnees = Etudiant.objects.all().values()
  donneesfiltres = Etudiant.objects.filter(prenom='djibril').values()
  nomdonnees = Etudiant.objects.filter(prenom__startswith='I').values()
  ordonnees = Etudiant.objects.all().order_by('nom').values()
  template = loader.get_template('template.html')
  context = {
    'mesdonnees': mesdonnees,
    'donneesfiltres': donneesfiltres,
    'nomdonnees': nomdonnees,
    'ordonnees': ordonnees,
  }
  return HttpResponse(template.render(context,request))



@authenticated
def connexion(request):
    if request.method == 'POST':
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            auth_login(request, user)

            if not hasattr(user, 'etudiant'):
                return redirect('profil_utilisateur')

            return redirect('home_connect')

        messages.info(request, "Nom d'utilisateur ou mot de passe incorrect.")

    return render(request, 'login.html')






def dossier(request):  return render(request ,'dossier.html')

def logout(request):
  auth_logout(request)
  return redirect('home')


@login_required
def profil_utilisateur(request):
    user = request.user

    etudiant, created = Etudiant.objects.get_or_create(utilisateur=user)

    formulaire = EtudiantForm(request.POST or None, request.FILES or None, instance=etudiant)

    if request.method == 'POST':
        if formulaire.is_valid():
            formulaire.save()
            return redirect('home_connect')

    return render(request, 'profil_utilisateur.html', {'formulaire': formulaire})






#administration

def administration(request):
    context = {

    }
    return render(request,'administration.html',context)

def etudiants(request , filiere_id):
    filiere = get_object_or_404(Filiere, id= filiere_id)
    etudiants = Etudiant.objects.filter(filiere=filiere)

    context = {
        'filiere': filiere ,
        'etudiants': etudiants
    }
    return render(request,'etudiants.html', context)

def details (request, id):
    etudiant = Etudiant.objects.get(id=id)
    form = AdminEtudiantForm(instance=etudiant)
    if request.method == 'POST':
        form = AdminEtudiantForm(request.POST, request.FILES, instance=etudiant)
        if form.is_valid():
            form.save()
    context = {
        'etudiant' : etudiant,
        'formulaire' : form
    }
    return render(request,'details.html',context)

def upload_cours(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Redirect to a success page
    else:
        form = DocumentForm()

    context = {
        'form' : form
    }
    return render(request, 'upload_cours.html', context)

def success_page(request):
    documents = Document.objects.all()
    context = {
        'documents' : documents,
    }
    return render(request, 'success_page.html', context)

def supprimer_etudiant(request, id):
    etudiant = get_object_or_404(Etudiant, id=id)
    filiere_id = etudiant.filiere.id if etudiant.filiere else None
    etudiant.delete()
    messages.success(request, "L’étudiant a été supprimé.")

    return redirect('etudiants', filiere_id=filiere_id)



#filière
def listeFilieres(request):
    filieres = Filiere.objects.all()
    context = {
        'filieres' : filieres
    }
    return render(request, 'listeFiliere.html',context)

def ajouter_filiere(request):
    if request.method == 'POST':
        form = FiliereForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listeFilieres')
    else:
        form = FiliereForm()
    return render(request, 'ajouter_filiere.html', {'form': form})

def ajouter_etudiant(request, filiere_id):
    filiere = get_object_or_404(Filiere, id=filiere_id)

    if request.method == "POST":
        prenom = request.POST.get("prenom")
        nom = request.POST.get("nom")
        telephone = request.POST.get("telephone")
        adresse = request.POST.get("adresse")
        date = request.POST.get("date")

        Etudiant.objects.create(
            prenom=prenom,
            nom=nom,
            telephone=telephone,
            adresse=adresse,
            date=date,
            filiere=filiere
        )

        return redirect("etudiants", filiere_id=filiere.id)

    return render(request, "ajouter_etudiant.html", {"filiere": filiere})

def page_recupcours(request):
    documents = Document.objects.all()
    context = {
        'documents' : documents,
    }
    return render(request, 'page_recupcours.html', context)
