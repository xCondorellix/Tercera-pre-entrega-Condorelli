from django.shortcuts import render
from .models import*
from django.http import HttpResponse
from .forms import *

# Create your views here.

def inicio(request):
    return HttpResponse("Bienvenido al inicio")

def asociados(request):
    
    if request.method == "POST":
        form = AsociadosForm(request.POST)
        if form.is_valid():
            asociado = Asociados()
            asociado.apellido_familia = form.cleaned_data ["apellido"]
            asociado.email = form.cleaned_data ["email"]
            asociado.DNI = form.cleaned_data ["DNI"]
            asociado.integrantes = form.cleaned_data ["integrantes"]
            asociado.mascotas = form.cleaned_data ["mascotas"]            
            form = AsociadosForm()
        else:
            pass
    else:
        form = AsociadosForm()
    
    asociados = Asociados.objects.all()
    context = {"asociados": asociados, "form": form}
    return render(request,"asociados.html", context)

def interes_terrenos(request):
    
    if request.method == "POST":
        form = TerrenosForm(request.POST)
        if form.is_valid():
            cliente = Terrenos()
            cliente.nombre = form.cleaned_data ["nombre"]
            cliente.apellido = form.cleaned_data ["apellido"]
            cliente.telefono= form.cleaned_data ["telefono"]
            cliente.email = form.cleaned_data ["email"]
            cliente.save()
            form = TerrenosForm()
        else:
            pass
    else:
        form = TerrenosForm()
    
    clientes = Terrenos.objects.all()
    context = {"clientes": clientes, "form": form}
    return render(request,"terrenos.html", context)

def participantes_torneos(request):

    if request.method == "POST":
        form = TorneoForm(request.POST)
        if form.is_valid():
            participante = Torneo()
            participante.nombre = form.cleaned_data ["nombre"]
            participante.apellido = form.cleaned_data ["apellido"]
            participante.email = form.cleaned_data ["email"]
            participante.DNI = form.cleaned_data ["DNI"]
            participante.save()
            form = TorneoForm()
        else:
            pass
    else:
        form = TorneoForm()

    participantes = Torneo.objects.all()
    context = {"participantes": participantes, "form": form}
    return render(request,"torneo.html", context)

def inicioAppbarrio(request):
    return render(request,"inicio.html")