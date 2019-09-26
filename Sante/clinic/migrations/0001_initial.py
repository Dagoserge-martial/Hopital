# Generated by Django 2.2.5 on 2019-09-24 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=225)),
                ('numero', models.IntegerField(max_length=12)),
                ('adresse', models.EmailField(max_length=254)),
                ('localisation', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('description', models.CharField(max_length=255)),
                ('text_footer', models.CharField(max_length=255)),
                ('soucrire_txt', models.CharField(max_length=255)),
                ('imageBner', models.ImageField(blank=True, upload_to='img')),
                ('imageCard', models.ImageField(blank=True, upload_to='img')),
                ('urlMap', models.URLField(max_length=255)),
                ('statut', models.BooleanField(default=True)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]