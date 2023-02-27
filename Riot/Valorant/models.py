from django.db import models

class Personagem(models.Model):
    nome = models.CharField(max_length=50)
    foto_pers = models.CharField(max_length=500) 
    descricao = models.CharField(max_length=2000) 
    
    