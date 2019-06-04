#!/usr/bin/env python
from pyweb.core.utils.runserver import runserver

SETTINGS_MODULE = "example.settings"


def main():
    runserver(SETTINGS_MODULE)


if __name__ == '__main__':
    main()
