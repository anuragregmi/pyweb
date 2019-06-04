import os
from importlib import import_module

from ..utils.lazy_object import LazyObject


class LazySetting(LazyObject):
    def setup(self, *args, **kwargs):
        self.instance = Setting()


class Setting:
    environment_name = "SETTINGS_MODULE"

    def __init__(self):
        settings_module = os.environ.get(self.environment_name)
        module = import_module(settings_module)

        for setting in dir(module):
            value = getattr(module, setting)
            setattr(self, setting, value)


settings = LazySetting()
