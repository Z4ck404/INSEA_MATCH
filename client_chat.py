#client_side
import socket
import select
import sys

def ip_inc(ip):
  L = ip.split(".")
  if(L[3]=='255') :
    L[3] = '0'
    if(L[2]=='255') :
      L[2] = '0'
      if(L[1]=='255') :
        L[1]= '0'
        L[0] = str(int(L[0])+1)
      else :
        L[1] = str(int(L[1])+1)
    else :
      L[2] = str(int(L[2])+1)
  else :
    L[3] = str(int(L[3])+1)
  ip = L[0]+'.'+L[1]+'.'+L[2]+'.'+L[3]
  return ip

def signal_handler(signum, frame):
  raise Exception("TimeOut")

def is_serv(ip):
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  signal.signal(signal.SIGALRM, signal_handler)
  signal.setitimer(signal.ITIMER_REAL,0.01)
  try:
    s.connect((ip,8091))
    r = True
  except Exception:
    r = False
  finally:
    s.close()
  return r

def check_rooms(ip_init="10.11.0.1",ip_last="10.11.3.255"):
  ip = ip_init
  L = []
  while(ip != ip_last) :
    if (is_serv(ip)):
      L += [ip]
    ip = ip_inc(ip)
  return L
 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) != 3:
    print ("Correct usage: script, IP address,name")
    exit()
IP_address = str(sys.argv[1])
Port = 8091
name = str(sys.argv[2])
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
sys.stdout.write("HI "+ sys.argv[2])

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
            sys.stdout.write("<"+ sys.argv[2] +">")
            sys.stdout.write(message)
            sys.stdout.flush()
server.close()
