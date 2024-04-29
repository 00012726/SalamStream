<<<<<<< HEAD
=======
"""
WSGI config for main_back project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

>>>>>>> 548ae16a45538045c502f85747dd4ad1fc58530f
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main_back.settings')

application = get_wsgi_application()
