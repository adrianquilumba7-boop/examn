"""
URL configuration for cine project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin as admin_original
from django.urls import path
from peliculas import views # Esta importación está bien

urlpatterns = [
    path('admin/', admin_original.site.urls),
    path('agregar/', views.agregar_pelicula, name='agregar_pelicula'),
    path('lista/', views.lista_peliculas, name='lista_peliculas'),
]