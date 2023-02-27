from faker import Faker
from django.shortcuts import render
from League_of_Legends.models import Personagem


def index(request):
    populator = Faker().text(),
    return render(request, 'League_of_Legends/paginas/index.html', 
    context={'sobre':populator,
        'listaPersonagem':Personagem.objects.all()})


