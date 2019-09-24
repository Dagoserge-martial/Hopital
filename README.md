# HOPITAL
 Dinamiser un  site d'hopital 

## Model

```
class Clinic (models.Model):
nom = models.CharField(max_length =225)
numero = models.IntegerField()
adresse = models.EmailField()
localisation = models.CharField(max_length=255)
email = models.EmailField(max_length=254)
description = models.CharField(max_length=255)
imageBner = models.ImageField(blank=True, upload_to='img')
imageCard = models.ImageField(blank=True, upload_to='img')
urlMap = models.URLField(max_length=255)
statut = models.BooleanField(default = True)
date_add = models.DateTimeField(auto_now_add= True)
date_update = models.DateTimeField(auto_now= True)

class logo (models.Model):
clinic = models.ForeignKey('Clinic', on_delete = models.CASCADE, related_name = 'clinic_bienvenue')
image = models.ImageField(blank=True, upload_to='img')
statut = models.BooleanField(default = True)
date_add = models.DateTimeField(auto_now_add= True)
date_update = models.DateTimeField(auto_now= True)

class ServiceClinic (models.Model):
clinic = models.ForeignKey('Clinic', on_delete = models.CASCADE, related_name = 'clinic_bienvenue')
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
clinic = models.ForeignKey('Clinic', on_delete = models.CASCADE, related_name = 'clinic_bienvenue')
icon = models.FAIconField()
titre = models.CharField(max_length =225)
description = models.CharField(max_length =225)
statut = models.BooleanField(default = True)
date_add = models.DateTimeField(auto_now_add= True)
date_update = models.DateTimeField(auto_now= True)

class Heur_travail (models.Model):
clinic = models.ForeignKey('Clinic', on_delete = models.CASCADE, related_name = 'clinic_bienvenue')
jour = models.DateTimeField(auto_now_add= True)
heur_arriv = models.DateTimeField(auto_now= True)
heur_dep = models.CharField(max_length =225)
statut = models.BooleanField(default = True)
date_add = models.DateTimeField(auto_now_add= True)
date_update = models.DateTimeField(auto_now= True)

class Docteur (models.Model):
clinic = models.ForeignKey('Clinic', on_delete = models.CASCADE, related_name = 'clinic_bienvenue')
nom = models.CharField(max_length =225)
image = models.ImageField(blank=True, upload_to='img')
description = models.CharField(max_length =225)
specialite = models.CharField(max_length =225)
urlSociaux = models.URLField(max_length=255)
statut = models.BooleanField(default = True)
date_add = models.DateTimeField(auto_now_add= True)
date_update = models.DateTimeField(auto_now= True)

class Reseaux_sociaux (models.Model):
docteur = models.ForeignKey('Docteur', on_delete = models.CASCADE, related_name = 'docteur_rsocial')
clinic = models.ForeignKey('Clinic', on_delete = models.CASCADE, related_name = 'docteur_rsocial')
titre = models.CharField(max_length =225)
statut = models.BooleanField(default = True)
date_add = models.DateTimeField(auto_now_add= True)
date_update = models.DateTimeField(auto_now= True)

class Temoignage (models.Model):
image_font = models.ForeignKey('Image_font', on_delete = models.CASCADE, related_name = 'font_temoin',)
user_id = models.ForeignKey('User', on_delete = models.CASCADE, related_name = 'user_temoignage')
titre = models.CharField(max_length =225)
description = models.CharField(max_length =225)
statut = models.BooleanField(default = True)
date_add = models.DateTimeField(auto_now_add= True)
date_update = models.DateTimeField(auto_now= True)


class Rendez_vous(models.Model):
image_font = models.ForeignKey('Image_font', on_delete = models.CASCADE, related_name = 'font_rdv',)
nom = models.CharField(max_length=50)
email = models.EmailField(max_length=255)
jours = models.DateField(auto_now=False, auto_now_add=False)
heure = models.TimeField(auto_now=False, auto_now_add=False)
nom_doctor = models.ForeignKey('Doctor', on_delete = models.CASCADE, related_name = 'doctor_rdv',)
message = models.CharField(max_length=255)
statut = models.BooleanField(default = True)
date_add = models.DateTimeField(auto_now_add= True)
date_update = models.DateTimeField(auto_now= True)

class Article_rdv(models.model):
titre = models.CharField(max_length=50)
image = models.ImageField(blank=True, upload_to='img')
description = models.CharField(max_length=255)
statut = models.BooleanField(default = True)
date_add = models.DateTimeField(auto_now_add= True)
date_update = models.DateTimeField(auto_now= True)

class Hebergement(models.model):
image_font = models.ForeignKey('Image_font', on_delete = models.CASCADE, related_name = 'font_rdv',)
titre = models.CharField(max_length=50)
prix = models.IntegerField()
description = models.CharField(max_length=255)
statut = models.BooleanField(default = True)
date_add = models.DateTimeField(auto_now_add= True)
date_update = models.DateTimeField(auto_now= True)

class Type_hebergement(models.model):
hebergement_id = models.ForeignKey('Hebergement', on_delete = models.CASCADE, related_name = 'hebergemnt_tp',)
titre = models.CharField(max_length=50)
nombre = models.IntegerField()
icon = icon = models.FAIconField()
statut = models.BooleanField(default = True)
date_add = models.DateTimeField(auto_now_add= True)
date_update = models.DateTimeField(auto_now= True)

class Image_font(models.model):
nom = models.CharField(max_length=50)
image = models.ImageField(blank=True, upload_to='font')
statut = models.BooleanField(default = True)
date_add = models.DateTimeField(auto_now_add= True)
date_update = models.DateTimeField(auto_now= True)

class Message(models.Model):
user_id = models.ForeignKey('User', on_delete = models.CASCADE, related_name = 'user_message',)
nom = models.CharField(max_length=255)
email = models.EmailField(max_length=254)
numero = models.PhoneNumberField()
sujet = models.CharField(max_length=255)
message = models.CharField(max_length=255)
statut = models.BooleanField(default = True)
date_add = models.DateTimeField(auto_now_add= True)
date_update = models.DateTimeField(auto_now= True)


```
