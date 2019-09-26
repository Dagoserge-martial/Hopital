from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Temoignage (models.Model):
    image_font = models.ForeignKey('Image_font', on_delete = models.CASCADE, related_name = 'font_temoin',)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'user_temoignage')
    titre = models.CharField(max_length =225)
    description = models.CharField(max_length =225)
    statut = models.BooleanField(default = True)
    date_add = models.DateTimeField(auto_now_add= True)
    date_update = models.DateTimeField(auto_now= True)

class Article_rdv(models.Model):
    titre = models.CharField(max_length=50)
    image = models.ImageField(blank=True, upload_to='img')
    description = models.CharField(max_length=255)
    statut = models.BooleanField(default = True)
    date_add = models.DateTimeField(auto_now_add= True)
    date_update = models.DateTimeField(auto_now= True)

class Hebergement(models.Model):
    image_font = models.ForeignKey('Image_font', on_delete = models.CASCADE, related_name = 'font_rdv',)
    titre = models.CharField(max_length=50)
    prix = models.IntegerField()
    description = models.CharField(max_length=255)
    statut = models.BooleanField(default = True)
    date_add = models.DateTimeField(auto_now_add= True)
    date_update = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.titre

class Type_hebergement(models.Model):
    hebergement_id = models.ForeignKey('Hebergement', on_delete = models.CASCADE, related_name = 'hebergemnt_tp',)
    titre = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    icon = models.CharField(max_length=525)
    statut = models.BooleanField(default = True)
    date_add = models.DateTimeField(auto_now_add= True)
    date_update = models.DateTimeField(auto_now= True)

class Message(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'user_message',)
    nom = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    numero = models.IntegerField()
    sujet = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    statut = models.BooleanField(default = True)
    date_add = models.DateTimeField(auto_now_add= True)
    date_update = models.DateTimeField(auto_now= True)

class Image_font(models.Model):
    nom = models.CharField(max_length=50)
    image = models.ImageField(blank=True, upload_to='font')
    statut = models.BooleanField(default = True)
    date_add = models.DateTimeField(auto_now_add= True)
    date_update = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.nom

#python manage.py admin_generator clinic >> clinic/admin.py