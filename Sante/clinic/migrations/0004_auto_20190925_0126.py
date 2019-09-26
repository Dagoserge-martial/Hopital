# Generated by Django 2.2.5 on 2019-09-25 01:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0003_logo_nom'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='heur_travail',
            name='icon',
        ),
        migrations.RemoveField(
            model_name='heur_travail',
            name='titre',
        ),
        migrations.AlterField(
            model_name='heur_travail',
            name='clinic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clinic_JHT', to='clinic.Clinic'),
        ),
        migrations.CreateModel(
            name='Travail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=225)),
                ('titre', models.CharField(max_length=225)),
                ('clinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clinic_HT', to='clinic.Clinic')),
            ],
        ),
    ]