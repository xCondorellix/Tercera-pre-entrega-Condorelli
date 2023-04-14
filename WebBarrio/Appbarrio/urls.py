from django.urls import path
from Appbarrio.views import *

urlpatterns = [
    path("",inicioAppbarrio, name="inicioApp"),
    path("propietarios/",propietarios, name= "propietarios"),
    path("visitas/",visitas, name= "visitas"),
    path("torneos/",torneos, name= "torneos"),
]
