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

'''
    From: https://docs.python.org/2/library/socketserver.html
'''
if __name__ == "__main__":
    # Port 0 means to select an arbitrary unused port
    HOST, PORT = "localhost", 0

    server = ThreadedDNSServer((HOST, PORT), ThreadedDNSRequestHandler)
    ip, port = server.server_address

    # Start a thread with the server -- that thread will then start one
    # more thread for each request
    server_thread = threading.Thread(target=server.serve_forever)
    # Exit the server thread when the main thread terminates
    server_thread.daemon = True
    server_thread.start()
    print("Server loop running in thread:", server_thread.name)

    server.shutdown()
    server.server_close()
