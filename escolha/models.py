from django.db import models

# Create your models here.

class Foto(models.Model):
    codigo_banco = models.CharField(max_length=200, null=False)
    nome = models.CharField(max_length=200)
    ano = models.CharField(max_length=200)
    comentario = models.CharField(max_length=200, blank=True, default='')
    imagem = models.ImageField(upload_to='escolha/static/escolha/images/',null=True, blank=True)
    escolhido = models.CharField(max_length=200, blank=True, default='')

    def __str__(self):
        return self.nome