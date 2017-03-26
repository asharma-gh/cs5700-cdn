import http.server
import socketserver as SocketServer
import threading

Handler = http.server.SimpleHTTPRequestHandler

class ThreadedHTTPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

class HTTPServerFront(object):
    server = 0
    def __init__(self, host, port):
        self.server = ThreadedHTTPServer((host, port), Handler)

        server_thread = threading.Thread(target=self.server.serve_forever)
        # Exit the server thread when the main thread terminates
        server_thread.daemon = True
        server_thread.start()
        print("Server loop running in thread:", server_thread.name)

        self.server.serve_forever()

        self.server.shutdown()
        self.server.server_close()

if __name__ == "__main__":
    baz = HTTPServerFront("localhost", 8000)
