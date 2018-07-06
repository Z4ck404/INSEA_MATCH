import socket
import select
import sys

from tools.functions import *

def clientthread(conn, addr):
 
    conn.send("--- you are connected ---")
 
    while True:
            try:
                message = conn.recv(2048)
                if message:
                    print ("<" + addr[0] + "> " + message)
                    message_to_send = "<" + addr[0] + "> " + message
                    broadcast(message_to_send, conn)
 
                else:
                    remove(conn)
 
            except:
                continue
def broadcast(message, connection):
    for clients in list_of_clients:
        if clients!=connection:
            try:
                clients.send(message)
            except:
                clients.close()
                remove(clients)
def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)