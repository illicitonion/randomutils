#!/usr/bin/env python
import base64
import cgi
import sys
import SocketServer
from BaseHTTPServer import BaseHTTPRequestHandler

class PasteBin(BaseHTTPRequestHandler):
    def do_POST(self):
        """Creates form['filename'] with contents base64-encoded parameter form['file']."""
        # curl -d "filename=/some/file&file=Zm9v" localhost:8080
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST',
                     'CONTENT_TYPE': self.headers['Content-Type']})
        f = open(form['filename'].value, 'w')
        f.write(base64.b64decode(form['file'].value))
        self.send_response(200)
        self.end_headers()
        self.wfile.write('Saved file %s\n' % form['filename'].value)

def main(args):
    try:
        port = int(args[1])
    except IndexError:
        print('Usage: pastebin.py port')
        sys.exit(1)
    except ValueError:
        print('Port must be a number')
        sys.exit(2)

    httpd = SocketServer.TCPServer(("", port), PasteBin)
    try:
        httpd.serve_forever()
    except:
        httpd.shutdown()

if __name__ == '__main__':
    main(sys.argv)
