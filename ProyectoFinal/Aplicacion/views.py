from django.shortcuts import render
from django.http import HttpResponse
from .models import (Cliente, Producto, Stock)

def Lista_Clientes(request):
    cliente = Cliente.objects.all().order_by('nombre')
    return render(request,'clientes/lista.html')

def Jugadores (request):
    return HttpResponse("Jugadores")
