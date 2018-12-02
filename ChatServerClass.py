"""
        SERVER for multithreaded (asynchronous) chat application.
"""

# using TCP socket fot this purpose, therefore uing AF_INET and SOCK_STREAM

from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

#   Constants setup for later use:

clients = {}
addresses = {}

HOST = ''
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

#   Accepting new connections method,
#   the following loop wil wait forever for incoming connections
def accept_incoming_connections():

    while True:
        client, client_address = SERVER.accept()

        print ("%s:%s has connected." % client_address)
        client.send(bytes("Greetings from Pychat 01!\n" +
                          "Now type your name and press enter!", "utf8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()

#   Handles a single client connection.
def handle_client(client):  #   takes client socket as argument
    name = client.recv(BUFSIZ).decode("utf8")
    welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit.' % name
    client.send(bytes(welcome, "utf8"))
    msg = '%s has joined the Chat! ' % name
    broadcast(bytes(msg, "utf8"))
    clients[client] = name
    while True:
        msg = client.recv(BUFSIZ)
        if msg != bytes("{quit}", "utf8"):
            broadcast(msg, name+": ")
        else:
            client.send(bytes("{quit}", "utf8"))
            client.close()
            del clients[client]
            broadcast(bytes("%s has left the chat." % name, "utf8"))
            break

#   Broadcast a message to all the clients.
def broadcast(msg, prefix=""):  # prefix is for name identification
    for sock in clients:
        sock.send(bytes(prefix, "utf8") + msg)

#   code for starting the server and listening for incoming connections:
if __name__ == "__main__":
    SERVER.listen(5)  # listens for 5 connections at max
    print("Waiting for connections...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start() #start the infinite loop
    # joing() ACCEPT_THREAD to that the main script waits for it to complete and doesn't jumtp to next line,
    # wich closes the server
    ACCEPT_THREAD.join()
    SERVER.close()
