# api/index.py
import os
import sys

# Caminhos para o projeto
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

from django.core.wsgi import get_wsgi_application
app = get_wsgi_application()
