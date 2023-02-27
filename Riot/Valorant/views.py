from django.shortcuts import render
from Valorant.models import Personagem

def index(request):
    return render(request, 'Valorant/paginas/index.html',
    context={'listaPersonagem':Personagem.objects.all()})