# Generated by Django 2.2.5 on 2019-09-25 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0004_auto_20190925_0126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reseaux_sociaux',
            name='docteur',
        ),
        migrations.AddField(
            model_name='reseaux_sociaux',
            name='docteur',
            field=models.ManyToManyField(to='clinic.Docteur'),
        ),
    ]