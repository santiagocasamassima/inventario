from django.shortcuts import render
from sistema_inventario.models import *
# Create your views here.

def listar_equipos(request):
    contexto = {
        "equipo": Equipos.objects.all()
    }
    http_response = render(
        request=request,
        template_name="equipos.base.html",
        context=contexto,
    )
    return http_response

