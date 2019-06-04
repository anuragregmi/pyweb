#!/usr/bin/env python

import sys
from wsgiref.simple_server import make_server

from pyweb.core.wsgi.application import Wsgi
import os


def runserver(settings_module):
    args_length = len(sys.argv)

    if args_length <= 1:
        host, port = 'localhost', 8000
    elif args_length == 2:
        host, port = 'localhost', int(sys.argv[1])
    else:
        host, port = sys.argv[1], int(sys.argv[2])

    os.environ.setdefault("SETTINGS_MODULE", settings_module)
    application = Wsgi()

    try:
        print("Starting server ...")
        httpd = make_server(host, port, application)
        print(f"Listening to {host}:{port}")
        print("Quit server with CONTROL-C")
        httpd.serve_forever()
    except OSError:
        print("Looks like the port you provided is already in use.")
    except KeyboardInterrupt:
        print()
        print("Turning Off the server ...")
        print("Server Turned Off")
