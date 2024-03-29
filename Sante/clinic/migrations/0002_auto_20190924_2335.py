# Generated by Django 2.2.5 on 2019-09-24 23:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Docteur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=225)),
                ('image', models.ImageField(blank=True, upload_to='img')),
                ('description', models.CharField(max_length=225)),
                ('specialite', models.CharField(max_length=225)),
                ('statut', models.BooleanField(default=True)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image_font',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='font')),
                ('statut', models.BooleanField(default=True)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='clinic',
            name='numero',
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name='Urgence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=225)),
                ('titre', models.CharField(max_length=225)),
                ('description', models.CharField(max_length=225)),
                ('statut', models.BooleanField(default=True)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('clinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clinic_urgence', to='clinic.Clinic')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceClinic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=225)),
                ('image', models.ImageField(blank=True, upload_to='img')),
                ('statut', models.BooleanField(default=True)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('clinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clinic_service', to='clinic.Clinic')),
            ],
        ),
        migrations.CreateModel(
            name='Reseaux_sociaux',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=225)),
                ('urlSociaux', models.URLField(max_length=255)),
                ('icon', models.CharField(max_length=225)),
                ('statut', models.BooleanField(default=True)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('clinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='docteur_rsocial', to='clinic.Clinic')),
                ('docteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='docteur_rsocial', to='clinic.Docteur')),
            ],
        ),
        migrations.CreateModel(
            name='Rendez_vous',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=255)),
                ('jours', models.DateField()),
                ('heure', models.TimeField()),
                ('message', models.CharField(max_length=255)),
                ('statut', models.BooleanField(default=True)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('image_font', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='font_rdv', to='clinic.Image_font')),
                ('nomdDoctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor_rdv', to='clinic.Docteur')),
            ],
        ),
        migrations.CreateModel(
            name='logo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='logo')),
                ('statut', models.BooleanField(default=True)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('clinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clinic_logo', to='clinic.Clinic')),
            ],
        ),
        migrations.CreateModel(
            name='Heur_travail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=225)),
                ('titre', models.CharField(max_length=225)),
                ('jour', models.DateField()),
                ('heur_debut', models.DateTimeField()),
                ('heur_fin', models.DateTimeField()),
                ('statut', models.BooleanField(default=True)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('clinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clinic_HT', to='clinic.Clinic')),
            ],
        ),
        migrations.AddField(
            model_name='docteur',
            name='clinic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clinic_docteur', to='clinic.Clinic'),
        ),
        migrations.CreateModel(
            name='Bienvenue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=225)),
                ('statut', models.BooleanField(default=True)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('clinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clinic_bienvenue', to='clinic.Clinic')),
            ],
        ),
    ]
