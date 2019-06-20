
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Hola mundo. Jose Almando es un crack. desde Jose")
