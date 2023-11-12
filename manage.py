# FRAMEWORK DJANGO
""" INSTALACION DE DJANGO
    Instalacion de django en CMD
        pip install Django==4.2.7
    Verificar la instalación de Django en CMD
        pip freeze // Se usa para mostrar 
        pip show django // Se usa para mostrar nombre, version, autor, ruta o localizacion, etc de django. La localizacion debe estar en la variable del sistema PYTHONPATH
    verificar la instalacion de django en python
        import django
        django.VERSION // Te muestra la version en forma de lista (4, 2, 7, 'final', 0)
"""
""" CREACION DE UN PROYECTO CON DJANGO EN CMD
    django-admin startproject NombreDel Proyecto // No debe comenzar con numero y no debe estar contenido con carpetas cuyos nombres comiencen en numero
"""

# manage.py
# Archivo generado automaticamente
# Comandos que se pueden realizar con este archivo
""" COMANDOS QUE SE PUEDEN REALIZAR CON EL ARCHIVO manage.py
    python manage.py runserver
    python manage.py migrate    // Busca las migraciones pendientes y las aplica a la base de datos. Si no hay migraciones pendientes, el comando no hace nada.
"""

#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os # Importando os para interactuar con el sistema operativo
import sys # Importando sys para interctuar con el interprete de python


def main(): # Definiendo las funcion principal
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FrameworkDjango.settings') # Estableciendo la variable de entorno DJANGO_SETTINGS_MODULE en el archivo FrameworkDjango.settings
    try:
        from django.core.management import execute_from_command_line # Importando el modulo execute_from_command_line del paquete django.core.management
    except ImportError as exc: # En caso hay un error de importacion
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv) # Llamando la funcion con argumento sys.argv


if __name__ == '__main__':
    main() # Llamando a la funcion main que se definio 
