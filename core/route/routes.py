from importlib import import_module

from ..conf.errors import ImproperlyConfigured


def get_routes(routes_path):
    mod = import_module(routes_path)
    if "routes" not in dir(mod):
        raise ImproperlyConfigured("Improperly Configured routs")
    return mod.routes
