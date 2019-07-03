from django.shortcuts import render
from .models import Foto

# from django.http import HttpResponse

def escolhidos(request):
    return render(request, 'escolha/escolhidos.html')

def naoEscohidos(request):
    result = Foto.objects.filter(escolhido=False)
    print(result[0].nome)
    return render(request, 'escolha/nao-escolhidos.html')

def home(request):
    return render(request, 'escolha/home.html')

