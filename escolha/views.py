from django.shortcuts import render
from .models import Foto

# from django.http import HttpResponse

def escolhidos(request):
    return render(request, 'escolha/escolhidos.html')

def escolhidosTable(request):
    print('Entrou')
    result = Foto.objects.filter(escolhido=False)
    print(result[0].imagem)
    string = result[0].nome
    return render(request, 'escolha/escolhidos-table.html', {"resultEscolhido": result})

def naoEscolhidos(request):
    print('template ' + request.GET.get('id'))
    print('Entrou')
    result = Foto.objects.filter(nome=request.GET.get('id'))
    print(result[0].imagem)
    return render(request, 'escolha/nao-escolhidos.html', {"resultNaoEscolhido": result, "nome": result[0].nome})

def naoEscolhidosTable(request):
    result = Foto.objects.filter(escolhido=False)
    return render(request, 'escolha/nao-escolhidos-table.html', {"resultNaoEscolhido": result})

def home(request):
    return render(request, 'escolha/home.html')

