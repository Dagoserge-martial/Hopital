from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Clinic (models.Model):
    nom = models.CharField(max_length =225)
    numero = models.IntegerField()
    adresse = models.EmailField()
    localisation = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    description = models.CharField(max_length=255)
    text_footer = models.CharField(max_length=255)
    soucrire_txt = models.CharField(max_length=255)
    imageBner = models.ImageField(blank=True, upload_to='img')
    imageCard = models.ImageField(blank=True, upload_to='img')
    urlMap = models.URLField(max_length=255)
    statut = models.BooleanField(default = True)
    date_add = models.DateTimeField(auto_now_add= True)
    date_update = models.DateTimeField(auto_now= True)

class logo (models.Model):
    clinic = models.ForeignKey('Clinic', on_delete = models.CASCADE, related_name = 'clinic_logo')
    image = models.ImageField(blank=True, upload_to='logo')
    statut = models.BooleanField(default = True)
    date_add = models.DateTimeField(auto_now_add= True)
    date_update = models.DateTimeField(auto_now= True)

class ServiceClinic (models.Model):
    clinic = models.ForeignKey('Clinic', on_delete = models.CASCADE, related_name = 'clinic_service')
    titre = models.CharField(max_length =225)
    image = models.ImageField(blank=True, upload_to='img')
    statut = models.BooleanField(default = True)
    date_add = models.DateTimeField(auto_now_add= True)
    date_update = models.DateTimeField(auto_now= True)

class Bienvenue (models.Model):
    clinic = models.ForeignKey('Clinic', on_delete = models.CASCADE, related_name = 'clinic_bienvenue')
    titre = models.CharField(max_length =225)
    statut = models.BooleanField(default = True)
    date_add = models.DateTimeField(auto_now_add= True)
    date_update = models.DateTimeField(auto_now= True)

class Urgence (models.Model):
    clinic = models.ForeignKey('Clinic', on_delete = models.CASCADE, related_name = 'clinic_urgence')
    image = models.ImageField(blank=True, upload_to='img')
    titre = models.CharField(max_length =225)
    description = models.CharField(max_length =225)
    statut = models.BooleanField(default = True)
    date_add = models.DateTimeField(auto_now_add= True)
    date_update = models.DateTimeField(auto_now= True)

class Heur_travail (models.Model):
    clinic = models.ForeignKey('Clinic', on_delete = models.CASCADE, related_name = 'clinic_HT')
    image = models.ImageField(blank=True, upload_to='img')
    titre = models.CharField(max_length =225)
    jour = models.DateField(auto_now_add= False)
    heur_debut = models.DateTimeField(auto_now= False)
    heur_fin = models.DateTimeField(auto_now_add= False)
    statut = models.BooleanField(default = True)
    date_add = models.DateTimeField(auto_now_add= True)
    date_update = models.DateTimeField(auto_now= True)

class Docteur (models.Model):
    clinic = models.ForeignKey('Clinic', on_delete = models.CASCADE, related_name = 'clinic_docteur')
    nom = models.CharField(max_length =225)
    image = models.ImageField(blank=True, upload_to='img')
    description = models.CharField(max_length =225)
    specialite = models.CharField(max_length =225)
    statut = models.BooleanField(default = True)
    date_add = models.DateTimeField(auto_now_add= True)
    date_update = models.DateTimeField(auto_now= True)  

class Reseaux_sociaux (models.Model):
    docteur = models.ForeignKey('Docteur', on_delete = models.CASCADE, related_name = 'docteur_rsocial')
    clinic = models.ForeignKey('Clinic', on_delete = models.CASCADE, related_name = 'docteur_rsocial')
    nom = models.CharField(max_length =225)
    urlSociaux = models.URLField(max_length=255)
    statut = models.BooleanField(default = True)
    date_add = models.DateTimeField(auto_now_add= True)
    date_update = models.DateTimeField(auto_now= True)