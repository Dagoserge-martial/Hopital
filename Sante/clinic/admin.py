# vim: set fileencoding=utf-8 :
from django.contrib import admin
from django.utils.safestring import mark_safe

from . import models


class ClinicAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'nom',
        'numero',
        'adresse',
        'localisation',
        'email',
        'imageBner',
        'imageCard',
        'urlMap',
        'statut',
        'date_add',
        'date_update',
    )
    list_filter = (
        'statut',
        'date_add',
        'date_update',
        'id',
        'nom',
        'numero',
        'adresse',
        'localisation',
        'email',
        'description',
        'text_footer',
        'soucrire_txt',
        'imageBner',
        'imageCard',
        'urlMap',
        'statut',
        'date_add',
        'date_update',
    )


class logoAdmin(admin.ModelAdmin):

    list_display = (
        'affiche_image',
        'id',
        'clinic',
        'nom',
        'image',
        'statut',
        'date_add',
        'date_update',
    )
    list_filter = (
        'clinic',
        'statut',
        'date_add',
        'date_update',
        'id',
        'clinic',
        'nom',
        'image',
        'statut',
        'date_add',
        'date_update',
    )
    def affiche_image(self, obj):
        return mark_safe('<img src = " {url} " width = " 100px " heigth = " 60px " />'.format(url= obj.image.url))


class ServiceClinicAdmin(admin.ModelAdmin):

    list_display = (
        'affiche_image',
        'id',
        'clinic',
        'titre',
        'image',
        'statut',
        'date_add',
        'date_update',
    )
    list_filter = (
        'clinic',
        'statut',
        'date_add',
        'date_update',
        'id',
        'clinic',
        'titre',
        'image',
        'statut',
        'date_add',
        'date_update',
    )
    def affiche_image(self, obj):
        return mark_safe('<img src = " {url} " width = " 60px " heigth = " 40px " />'.format(url= obj.image.url))

class BienvenueAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'clinic',
        'titre',
        'statut',
        'date_add',
        'date_update',
    )
    list_filter = (
        'clinic',
        'statut',
        'date_add',
        'date_update',
        'id',
        'clinic',
        'titre',
        'statut',
        'date_add',
        'date_update',
    )


class UrgenceAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'clinic',
        'icon',
        'titre',
        'description',
        'statut',
        'date_add',
        'date_update',
    )
    list_filter = (
        'clinic',
        'statut',
        'date_add',
        'date_update',
        'id',
        'clinic',
        'icon',
        'titre',
        'description',
        'statut',
        'date_add',
        'date_update',
    )

class TravailAdmin(admin.ModelAdmin):
    
    list_display = (
        'id',
        'clinic',
        'titre',
        'icon',
    )
    list_filter = (
        'clinic',
        'id',
        'clinic',
    )

class Heur_travailAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'clinic',
        'jour',
        'heur_debut',
        'heur_fin',
        'statut',
        'date_add',
        'date_update',
    )
    list_filter = (
        'clinic',
        'jour',
        'heur_debut',
        'heur_fin',
        'statut',
        'date_add',
        'date_update',
        'id',
        'clinic',
        'jour',
        'heur_debut',
        'heur_fin',
        'statut',
        'date_add',
        'date_update',
    )


class DocteurAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'clinic',
        'nom',
        'image',
        'description',
        'specialite',
        'statut',
        'date_add',
        'date_update',
    )
    list_filter = (
        'clinic',
        'statut',
        'date_add',
        'date_update',
        'id',
        'clinic',
        'nom',
        'image',
        'description',
        'specialite',
        'statut',
        'date_add',
        'date_update',
    )


class Reseaux_sociauxAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'clinic',
        'nom',
        'urlSociaux',
        'icon',
        'statut',
        'date_add',
        'date_update',
    )
    list_filter = (
        'clinic',
        'statut',
        'date_add',
        'date_update',
        'id',
        'docteur',
        'clinic',
        'nom',
        'urlSociaux',
        'icon',
        'statut',
        'date_add',
        'date_update',
    )


class Rendez_vousAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'image_font',
        'nom',
        'email',
        'jours',
        'heure',
        'nomdDoctor',
        'message',
        'statut',
        'date_add',
        'date_update',
    )
    list_filter = (
        'image_font',
        'jours',
        'nomdDoctor',
        'statut',
        'date_add',
        'date_update',
        'id',
        'image_font',
        'nom',
        'email',
        'jours',
        'heure',
        'nomdDoctor',
        'message',
        'statut',
        'date_add',
        'date_update',
    )


class Image_fontAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'nom',
        'image',
        'statut',
        'date_add',
        'date_update',
    )
    list_filter = (
        'statut',
        'date_add',
        'date_update',
        'id',
        'nom',
        'image',
        'statut',
        'date_add',
        'date_update',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Clinic, ClinicAdmin)
_register(models.logo, logoAdmin)
_register(models.ServiceClinic, ServiceClinicAdmin)
_register(models.Bienvenue, BienvenueAdmin)
_register(models.Urgence, UrgenceAdmin)
_register(models.Travail, TravailAdmin)
_register(models.Heur_travail, Heur_travailAdmin)
_register(models.Docteur, DocteurAdmin)
_register(models.Reseaux_sociaux, Reseaux_sociauxAdmin)
_register(models.Rendez_vous, Rendez_vousAdmin)
_register(models.Image_font, Image_fontAdmin)
