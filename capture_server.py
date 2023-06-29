"""
# Python 3 server example
"""
import logging
from http.server import BaseHTTPRequestHandler, HTTPServer


logger = logging.getLogger(__name__)

HOSTNAME = ""
PORT = 8080


"""
MyServer Class
"""
class MyServer(BaseHTTPRequestHandler):
    def do_get(self):
        """
        do get
        """
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title> \
                               https://pythonbasics.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        logging.info(self.path)
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))


def run_server(host_name="", server_port=8080):
    """
    main function
    """
    web_server = HTTPServer((host_name, server_port), MyServer)
    print("Server started http://%s:%s" % (host_name, server_port))

    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        pass

    web_server.server_close()
    print("Server stopped.")


if __name__ == "__main__":
    run_server(HOSTNAME, PORT)
