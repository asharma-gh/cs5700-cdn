import socketserver as SocketServer
import socket
import threading
'''
Represents a basic DNS Server, with dynamic IP redirection
for load-balancing and performance
@authors Arvin Sharma, Cbrown
@license AGPLv3
'''

class ThreadedDNSRequestHandler(SocketServer.BaseRequestHandler):
    '''
        handler for incoming packets for this server,
        assumes that we will receive DNS messages
    '''
    def handle(self):
        return "fiz"

class ThreadedDNSServer(SocketServer.ThreadingMixIn, SocketServer.UDPServer):
    '''
        Multi-threaded server for performance, should make things faster
        Gonna just go with all the inherited stuff, so nothing is here!
    '''
    pass

class DNSServerFront(object):
    '''
        Represents the front-end interface for the DNS Server
    '''
    # server object
    server = 0

    def __init__(self,host, port):
        self.server = ThreadedDNSServer((host, port), ThreadedDNSRequestHandler)
        # Start a thread with the server -- that thread will then start one
        # more thread for each request
        server_thread = threading.Thread(target=self.server.serve_forever)
        # Exit the server thread when the main thread terminates
        server_thread.daemon = True
        server_thread.start()
        print("Server loop running in thread:", server_thread.name)

        self.server.shutdown()
        self.server.server_close()


'''
    From: https://docs.python.org/2/library/socketserver.html
'''
if __name__ == "__main__":
    foo = DNSServerFront("localhost", 0)
