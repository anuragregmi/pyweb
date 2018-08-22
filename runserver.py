#!/usr/bin/env python

import sys
from wsgiref.simple_server import make_server

from core.wsgi.application import Wsgi


def main():
    args_length = len(sys.argv)

    if args_length <= 1:
        host, port = 'localhost', 8000

    elif args_length == 2:
        host, port = sys.argv[0], 8000

    else:
        host, port = sys.argv[0], int(sys.argv[1])

    application = Wsgi()
    httpd = make_server(host, port, application)
    print(f"Listening to {host}:{port}")
    httpd.serve_forever()


if __name__ == '__main__':
    main()
