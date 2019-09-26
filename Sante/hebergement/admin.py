# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class TemoignageAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'image_font',
        'user_id',
        'titre',
        'description',
        'statut',
        'date_add',
        'date_update',
    )
    list_filter = (
        'image_font',
        'user_id',
        'statut',
        'date_add',
        'date_update',
        'id',
        'image_font',
        'user_id',
        'titre',
        'description',
        'statut',
        'date_add',
        'date_update',
    )


class Article_rdvAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'titre',
        'image',
        'description',
        'statut',
        'date_add',
        'date_update',
    )
    list_filter = (
        'statut',
        'date_add',
        'date_update',
        'id',
        'titre',
        'image',
        'description',
        'statut',
        'date_add',
        'date_update',
    )


class HebergementAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'image_font',
        'titre',
        'prix',
        'description',
        'statut',
        'date_add',
        'date_update',
    )
    list_filter = (
        'image_font',
        'statut',
        'date_add',
        'date_update',
        'id',
        'image_font',
        'titre',
        'prix',
        'description',
        'statut',
        'date_add',
        'date_update',
    )


class Type_hebergementAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'hebergement_id',
        'titre',
        'nombre',
        'icon',
        'statut',
        'date_add',
        'date_update',
    )
    list_filter = (
        'hebergement_id',
        'statut',
        'date_add',
        'date_update',
        'id',
        'hebergement_id',
        'titre',
        'nombre',
        'icon',
        'statut',
        'date_add',
        'date_update',
    )


class MessageAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'user_id',
        'nom',
        'email',
        'numero',
        'sujet',
        'message',
        'statut',
        'date_add',
        'date_update',
    )
    list_filter = (
        'user_id',
        'statut',
        'date_add',
        'date_update',
        'id',
        'user_id',
        'nom',
        'email',
        'numero',
        'sujet',
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


_register(models.Temoignage, TemoignageAdmin)
_register(models.Article_rdv, Article_rdvAdmin)
_register(models.Hebergement, HebergementAdmin)
_register(models.Type_hebergement, Type_hebergementAdmin)
_register(models.Message, MessageAdmin)
_register(models.Image_font, Image_fontAdmin)
