#client_side
import socket
import select
import sys

from tools.client_helper import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) != 2:
    print ("Correct usage: script, name")
    exit()
#IP_address = str(sys.argv[1])
Port = 8091
name = str(sys.argv[1])
IP_address = choose_room()
server.connect((IP_address, Port))

print ("""
  _____ _   _  _____ ______            __  __       _______ _____ _    _ 
 |_   _| \ | |/ ____|  ____|   /\     |  \/  |   /\|__   __/ ____| |  | |
   | | |  \| | (___ | |__     /  \    | \  / |  /  \  | | | |    | |__| |
   | | | . ` |\___ \|  __|   / /\ \   | |\/| | / /\ \ | | | |    |  __  |
  _| |_| |\  |____) | |____ / ____ \  | |  | |/ ____ \| | | |____| |  | |
 |_____|_| \_|_____/|______/_/    \_\ |_|  |_/_/    \_\_|  \_____|_|  |_|
                                  ______                                 
                                 |______|                                

""")
print("the first local social network in INSEA ") 
sys.stdout.write("HI "+ sys.argv[1])

while True:
    sockets_list = [sys.stdin, server]
    read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])
 
    for socks in read_sockets:
        if socks == server:
            message = socks.recv(2048)
            print (message)
        else:
            message = sys.stdin.readline()
            server.send(message)
            sys.stdout.write("<"+ sys.argv[1] +">")
            sys.stdout.write(message)
            sys.stdout.flush()
server.close()
