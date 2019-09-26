from django.shortcuts import render
from .models import *
from hebergement.models import *

# Create your views here.

def home(request):
    cline = Clinic.objects.filter(statut=True)
    article = Article_rdv.objects.filter(statut=True)
    temoignage = Temoignage.objects.filter(statut=True)
    bienvenue = Bienvenue.objects.filter(statut=True)
    hebergent = Hebergement.objects.filter(statut=True)
    data = {
        'cline': cline,
        'article': article,
        'temoignage' : temoignage,
        'bienvenue' : bienvenue,
        'hebergent': hebergent,
    }

    if request.method == 'POST':
        nom = request.POST.get('username')
        numero = request.POST.get('phone')
        sujet = request.POST.get('sujet')
        message = request.POST.get('message')
        email = request.POST.get('email')
        # p = Person(nom=nom, numero=numero,email=email, sujet=sujet, message=message)
        # p.save()
        print(nom)
        print(numero)
        print(email)
        print(sujet)
        print(message)
        return render(request, 'index.html') 
    else: 
        return render(request, 'index.html')

    return render(request, 'index.html', data)
