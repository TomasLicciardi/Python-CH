from django.http import HttpResponse
from django.shortcuts import render
from .models import Miembro_Familiar
# Create your views here.

def inicioApp(request):
    return render(request, 'AppMvt/index.html')

def crear_miembro_familiar(request):
    persona=Miembro_Familiar( nombre='Juan' , apellido='Gonzales' , edad=39 , fecha_de_nacimiento = '1982-08-18' )
    persona.save()

    persona=Miembro_Familiar( nombre='Jose' , apellido='Zidane' , edad=17 , fecha_de_nacimiento = '2005-03-17' )
    persona.save()
    
    persona=Miembro_Familiar( nombre='Enzo' , apellido='Fernandez', edad=23 , fecha_de_nacimiento = '1999-04-24' )
    persona.save()

    texto= f"Se creo el familiar {persona.nombre} {persona.apellido}, con edad {persona.edad} , nacida en el {persona.fecha_de_nacimiento}"
    return HttpResponse(texto)

def familiares(request):
    familiares = Miembro_Familiar.objects.all()
    return render(request, 'AppMvt/familia.html', context={'familiares':familiares})