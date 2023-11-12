# urls.py
# Archivo generado automaticamente

"""
URL configuration for FrameworkDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin # Importando el modulo admin
from django.urls import path # Importando el modulo path

urlpatterns = [ # Defniniendo una lista que contiene la ruta que es la instancia de la clase path
    path('admin/', admin.site.urls), # Definicendo una instancia de la clase Path. La función site.urls devuelve un objeto URLResolver que maneja las solicitudes de URL para la aplicación de administración de Django
] # Ruta que define la URL: http://localhost:8000/admin/
