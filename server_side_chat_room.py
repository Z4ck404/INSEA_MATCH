#server_side
import socket
import select
import sys
from thread import *

from tools.server_helper import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
"""
if len(sys.argv) != 3:
    print ( "Correct usage: script, IP address, port number")
    exit()
"""
IP_address = getIPaddr()
Port = 8091
server.bind((IP_address, Port))
server.listen(100)
 
list_of_clients = []
 
while True:
    conn, addr = server.accept()
    list_of_clients.append(conn)
    print (addr[0] + " connected")
    start_new_thread(clientthread,(conn,addr))    
 
conn.close()
server.close()