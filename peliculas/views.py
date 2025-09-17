
from django.shortcuts import render, redirect
from .forms import PeliculaForm
from .models import Pelicula


def agregar_pelicula(request):
    
    if request.method == 'POST':
        form = PeliculaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_peliculas')  
    else:
        
        form = PeliculaForm()
    
    return render(request, 'peliculas/agregar_pelicula.html', {'form': form})
    
def lista_peliculas(request):
    peliculas = Pelicula.objects.all() 
    return render(request, 'peliculas/lista_peliculas.html', {'peliculas': peliculas})