from core.wsgi.application import Wsgi
import os

os.environ.setdefault("SETTINGS_MODULE", 'example.settings')
application = Wsgi()
