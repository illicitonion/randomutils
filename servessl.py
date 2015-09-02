#!/usr/bin/python2
import BaseHTTPServer, SimpleHTTPServer
import os
import ssl
import sys

if len(sys.argv) != 4:
    sys.stderr.write("Usage: %s port certfile keyfile\n" % sys.argv[0])
    os._exit(2)

port = int(sys.argv[1])
certfile = sys.argv[2]
keyfile = sys.argv[3]

httpd = BaseHTTPServer.HTTPServer(('', port), SimpleHTTPServer.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket, certfile=certfile, keyfile=keyfile, server_side=True)
httpd.serve_forever()
