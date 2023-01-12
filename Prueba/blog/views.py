from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def saludo(request):
    return HttpResponse("Esta la primera página del blog")

def despedida(request):
    return HttpResponse("Esta es la página de despedida")