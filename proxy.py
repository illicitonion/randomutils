#!/usr/bin/env python
import sys
import urllib
import SimpleHTTPServer
import SocketServer

class Proxy(SimpleHTTPServer.SimpleHTTPRequestHandler):
  def do_GET(self):
    print(self.requestline)
    for (k,v) in self.headers.items():
        print('%s: %s' % (k, v))
    print('')
    self.copyfile(urllib.urlopen(self.path), self.wfile)


def main(args):
    try:
        port = int(args[1])
    except IndexError:
        print('Usage: %s port' % args[0])
        sys.exit(1)
    except ValueError:
        print('Port must be a number')
        sys.exit(2)

    httpd = SocketServer.TCPServer(("", port), Proxy)
    try:
        httpd.serve_forever()
    except:
        httpd.shutdown()

if __name__ == '__main__':
    main(sys.argv)
