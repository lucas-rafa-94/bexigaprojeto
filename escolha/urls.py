from django.urls import path
from . import views

urlpatterns = [
    path('escolhidos', views.escolhidos, name='escolhidos'),
    path('', views.home, name='home'),
    path('nao-escolhidos', views.naoEscohidos, name='nao-escolhidos')
]