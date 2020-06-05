"""
WSGI config for cargo_management_system project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""
#activate_env = '/home/gurdayal-s/Desktop/hello_world/project/cargo_management_system/venv/bin/activate_this.py'
#exec(open(activate_env).read(),dict(__file__=activate_env))

import os
import sys
import site

# Add site packages
#site.addsitedir('/home/gurdayal-s/Desktop/hello_world/project/cargo_management_system/venv/lib/python3.6/site-packages')

# Add app dir to PYTHONPATH
#sys.path.append('/home/gurdayal-s/Desktop/hello_world/project/cargo_management_system')
#sys.path.append('/home/gurdayal-s/Desktop/hello_world/project/cargo_management_system/cargo_management_system')

# Set enviroment setting
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cargo_management_system.settings')

# Activate Venv


from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
