from django.apps import AppConfig

class MyfirstappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myFirstApp'

def ready(self):
    self.create_default_groups()

def create_default_groups(self):
    group_names = [ 'Etudiant', 'Responsable']
    for name in group_names:
        Group.objects.get_or_create(name=name)