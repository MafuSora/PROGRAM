"""
WSGI config for firstweb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'firstweb.settings')


# import os

# from django.core.wsgi import get_wsgi_application

# # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_skripsi.settings')
# os.environ['DJANGO_SETTINGS_MODULE']= 'web_skripsi.settings'
application = get_wsgi_application()
app = application