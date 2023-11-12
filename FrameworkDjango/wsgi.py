# wsgi.py
# Archivo generado automaticamente
# Se encarga de configurar una aplicacion web de Django para que se ejecute en un servidor WSGI (Web Server Gateway Interface), el cual describe como se comunica una aplicacion web con un servidor web
"""
WSGI config for FrameworkDjango project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os # Importando os para interactuar con el sistema operativo

from django.core.wsgi import get_wsgi_application # Importando la funcion que devuelve una instancia de la clase WSGIHandler para manejar las colicitudes de la aplicacion web

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FrameworkDjango.settings') # establece la variable de entorno DJANGO_SETTINGS_MODULE en 'FrameworkDjango.settings', el cual le dice a Django qué archivo de configuración de la aplicación usar.

application = get_wsgi_application() # Otorgando el manejo de de la solicitudes de la aplicacion web
