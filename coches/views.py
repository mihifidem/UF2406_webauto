from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Bienvenido a la API de Coches de Segunda Mano 🚗</h1>")
