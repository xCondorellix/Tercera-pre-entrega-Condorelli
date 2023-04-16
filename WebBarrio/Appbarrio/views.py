from django.shortcuts import render
from .models import*
from django.http import HttpResponse
from .forms import *

# Create your views here.

def inicio(request):
    return HttpResponse("Bienvenido al inicio")

def asociados(request):
    return render(request,"asociados.html")

def interes_terrenos(request):
    return render(request,"terrenos.html")

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