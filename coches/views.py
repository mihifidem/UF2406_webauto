from django.http import HttpResponse
from rest_framework import viewsets
from .models import Coche
from .serializers import CocheSerializer

class CocheViewSet(viewsets.ModelViewSet):
    queryset = Coche.objects.all()
    serializer_class = CocheSerializer

def home(request):
    return HttpResponse("<h1>Bienvenido a la API de Coches de Segunda Mano 🚗</h1>")
