# HOPITAL
 Dinamiser un  site d'hopital 

## Model

```
class Clinic (models.Model):
nom = models.CharFiel(max_length =225)
numero = models.PhoneNumberField()
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
titre = models.CharFiel(max_length =225)
statut = models.BooleanField(default = True)
date_add = models.DateTimeField(auto_now_add= True)
date_update = models.DateTimeField(auto_now= True)


class Bienvenue (models.Model):
clinic = models.ForeignKey('Clinic', on_delete = models.CASCADE, related_name = 'clinic_bienvenue')
titre = models.CharFiel(max_length =225)
statut = models.BooleanField(default = True)
date_add = models.DateTimeField(auto_now_add= True)
date_update = models.DateTimeField(auto_now= True)

class Urgence (models.Model):
clinic = models.ForeignKey('Clinic', on_delete = models.CASCADE, related_name = 'clinic_bienvenue')
icon = models.FAIconField()
titre = models.CharFiel(max_length =225)
description = models.CharFiel(max_length =225)
statut = models.BooleanField(default = True)
date_add = models.DateTimeField(auto_now_add= True)
date_update = models.DateTimeField(auto_now= True)

class Docteur (models.Model):
clinic = models.ForeignKey('Clinic', on_delete = models.CASCADE, related_name = 'clinic_bienvenue')
nom = models.CharFiel(max_length =225)
image = models.ImageField(blank=True, upload_to='img')
description = models.CharFiel(max_length =225)
specialite = models.CharFiel(max_length =225)
urlSociaux = models.URLField(max_length=255)
statut = models.BooleanField(default = True)
date_add = models.DateTimeField(auto_now_add= True)
date_update = models.DateTimeField(auto_now= True)

class Reseaux_sociaux (models.Model):
docteur = models.ForeignKey('Docteur', on_delete = models.CASCADE, related_name = 'docteur_rsocial')
clinic = models.ForeignKey('Clinic', on_delete = models.CASCADE, related_name = 'docteur_rsocial')
titre = models.CharFiel(max_length =225)
statut = models.BooleanField(default = True)
date_add = models.DateTimeField(auto_now_add= True)
date_update = models.DateTimeField(auto_now= True)

class Temoignage (models.Model):
user_id = models.ForeignKey('User', on_delete = models.CASCADE, related_name = 'user_temoignage')
titre = models.CharFiel(max_length =225)
description = models.CharFiel(max_length =225)
statut = models.BooleanField(default = True)
date_add = models.DateTimeField(auto_now_add= True)
date_update = models.DateTimeField(auto_now= True)

```
