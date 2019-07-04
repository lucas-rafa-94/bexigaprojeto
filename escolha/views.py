from django.shortcuts import render
from .models import Foto

from django.http import HttpResponse

def escolhidos(request):
    if request.method == 'GET':
        result = Foto.objects.filter(nome=request.GET.get('id'))
        print(result[0].escolhido)
        return render(request, 'escolha/escolhidos.html',
                      {"resultEscolhido": result, "nome": result[0].nome, "id": result[0].codigo_banco,
                       "comentario": result[0].comentario, "escolhido": result[0].escolhido})
    else:
        aprovado_ = False
        if request.POST.get('aprovado') == 'on':
            aprovado_ = True
        Foto.objects.filter(codigo_banco=request.GET.get('id')).update(comentario=request.POST.get('comentario'),escolhido=aprovado_)
        print('Entrouuuuuu')
        result = Foto.objects.filter(escolhido=True).values('nome', 'codigo_banco').distinct()
        return render(request, 'escolha/escolhidos-table.html', {"resultEscolhido": result})

def escolhidosTable(request):
    result = Foto.objects.filter(escolhido=True).values('nome', 'codigo_banco').distinct()
    return render(request, 'escolha/escolhidos-table.html', {"resultEscolhido": result})

def naoEscolhidos(request):
    if request.method == 'GET':
        result = Foto.objects.filter(nome=request.GET.get('id'))
        return render(request, 'escolha/nao-escolhidos.html', {"resultNaoEscolhido": result, "nome": result[0].nome, "id": result[0].codigo_banco,
                                                               "comentario": result[0].comentario, "escolhido": result[0].escolhido  })
    else:
        aprovado_ = False
        if request.POST.get('aprovado') == 'on':
            aprovado_ = True
        Foto.objects.filter(codigo_banco=request.GET.get('id')).update(comentario=request.POST.get('comentario'), escolhido=aprovado_)
        result = Foto.objects.filter(escolhido=False).values('nome', 'codigo_banco').distinct()
        return render(request, 'escolha/nao-escolhidos-table.html', {"resultNaoEscolhido": result} )

def naoEscolhidosTable(request):
    result = Foto.objects.filter(escolhido=False).values('nome', 'codigo_banco').distinct()
    return render(request, 'escolha/nao-escolhidos-table.html', {"resultNaoEscolhido": result})

def home(request):
    result = Foto.objects.all().values('nome', 'codigo_banco', 'escolhido').distinct()
    return render(request, 'escolha/home.html', {"result": result})

def todos(request):
    if request.method == 'GET':
        result = Foto.objects.filter(nome=request.GET.get('id'))
        return render(request, 'escolha/todos.html',
                      {"result": result, "nome": result[0].nome, "id": result[0].codigo_banco,
                       "comentario": result[0].comentario, "escolhido": result[0].escolhido})
    else:
        aprovado_ = False
        if request.POST.get('aprovado') == 'on':
            aprovado_ = True
        print(aprovado_)
        Foto.objects.filter(codigo_banco=request.GET.get('id')).update(comentario=request.POST.get('comentario'),escolhido=aprovado_)
        result = Foto.objects.all().values('nome', 'codigo_banco', 'escolhido').distinct()
        return render(request, 'escolha/home.html', {"result": result})

