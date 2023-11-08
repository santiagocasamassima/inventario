from django.contrib import admin
from django.urls import path
from sistema_inventario.views import listar_equipos

urlpatterns = [
    path('equipos/', listar_equipos),
    
]