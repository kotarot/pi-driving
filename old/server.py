#!/usr/bin/env python

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

PORT = 8000

class myHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print self.path
        if self.path == '/':
            with open('index.html', 'r') as file:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(file.read())
        return

try:
    server = HTTPServer(('', PORT), myHandler)
    server.serve_forever()
except KeyboardInterrupt:
    server.socket.close()
