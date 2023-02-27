from django.db import models

class Roles(models.Model): 
    nome = models.CharField(max_length=50)  

class Personagem(models.Model):
    nome = models.CharField(max_length=50)
    foto_pers = models.CharField(max_length=500) 
    descricao = models.CharField(max_length=2000) 
    role =  models.ForeignKey(Roles, on_delete=models.DO_NOTHING, default=None, null=True)

