from django.urls import path
from Appbarrio.views import *

urlpatterns = [
    path("",inicioAppbarrio),
    path("propietarios/",propietarios),
    path("visitas/",visitas),
    path("torneos/",torneos),
]
