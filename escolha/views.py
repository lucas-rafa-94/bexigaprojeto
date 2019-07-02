from django.shortcuts import render

# from django.http import HttpResponse

def escolhidos(request):
    return render(request, 'escolha/escolhidos.html')

def naoEscohidos(request):
    return render(request, 'escolha/nao-escolhidos.html')

def home(request):
    return render(request, 'escolha/home.html')

