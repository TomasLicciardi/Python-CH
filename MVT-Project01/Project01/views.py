from unittest import loader
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.



def inicio(request):
    return HttpResponse ('Pagina de inicio MVT-Project')
