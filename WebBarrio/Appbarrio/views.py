from django.shortcuts import render
from .models import*
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return HttpResponse("Bienvenido al inicio")

def propietarios(request):
    return render(request,"propietarios.html")

def visitas(request):
    return render(request,"visitas.html")

def torneos(request):
    return render(request,"torneos.html")

def inicioAppbarrio(request):
    return render(request,"inicio.html")