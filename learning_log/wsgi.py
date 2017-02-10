"""
WSGI config for learning_log project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
# Impor Cling which helps serve static files correct and use it to launch the
# application
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_log.settings")
application = get_wsgi_application()
application = DjangoWhiteNoise(application)
