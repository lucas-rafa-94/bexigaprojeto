from django.urls import path
from . import views

urlpatterns = [
    path('escolhidos', views.escolhidos, name='escolhidos'),
    path('escolhidos-table', views.escolhidosTable, name='escolhidos-table'),
    path('', views.home, name='home'),
    path('nao-escolhidos', views.naoEscolhidos, name='nao-escolhidos'),
    path('nao-escolhidos-table', views.naoEscolhidosTable, name='nao-escolhidos-table')
]