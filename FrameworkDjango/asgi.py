# asgi.py
# Archivo generado automaticamente

"""
ASGI config for FrameworkDjango project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os # Importando os para interactuar con el sistema operativo

from django.core.asgi import get_asgi_application # Importando get_asgi_application() para obtener la aplicacion ASGI de Django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FrameworkDjango.settings') # Estableciendo la la variable de entorno DJANGO_SETTINGS_MODULE en el archivo FrameworkDjango.settings

application = get_asgi_application() # Llamando a la funcion get_asgi_application() para establecer el resultado en la variable application
