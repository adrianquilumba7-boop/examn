from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import PeliculaForm
from .models import Pelicula

from django.shortcuts import render

def agregar_pelicula(request):
    
    return render(request, 'peliculas/agregar_pelicula.html', {})

def lista_peliculas(request):
    
    return render(request, 'peliculas/lista_peliculas.html', {})