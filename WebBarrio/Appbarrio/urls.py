from django.urls import path
from Appbarrio.views import *

urlpatterns = [
    path("",inicioAppbarrio, name="inicioApp"),
    path("asociados/",asociados, name= "asociados"),
    path("terrenos/",interes_terrenos, name= "terrenos"),
    path("torneo/",participantes_torneos, name= "torneo"),
]
