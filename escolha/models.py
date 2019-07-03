from django.db import models

# Create your models here.

class Foto(models.Model):
    nome = models.CharField(max_length=200)
    ano = models.CharField(max_length=200)
    comentario = models.CharField(max_length=200)
    imagem = models.ImageField(upload_to='escolha/static/escolha/images/',null=True, blank=True)
    escolhido = models.BooleanField(default=None)

    def __str__(self):
        return self.nome