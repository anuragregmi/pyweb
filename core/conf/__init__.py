import os
from importlib import import_module


class Setting:
    environment_name = "SETTINGS_MODULE"

    def __init__(self):
        settings_module = os.environ.get(self.environment_name)
        module = import_module(settings_module)

        for setting in dir(module):
            value = getattr(module, setting)
            setattr(self, setting, value)


# settings = Setting()
settings = type("Settings", tuple(), {})()
