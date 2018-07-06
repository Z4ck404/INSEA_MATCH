import socket
import select
import sys
import signal

from netifaces import AF_INET, AF_INET6, AF_LINK, AF_PACKET, AF_BRIDGE
import netifaces as ni

from tools.functions import *

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

def getInterface(ip):
  for inf in ni.interfaces():
    if(ni.ifaddresses(inf)[AF_INET][0]['addr'] == ip):
      return inf
  exit()

def convertMask(mask):
  M = mask.split(".")
  msk = 0
  for i in M :
    i = bin(int(i))[2:]
    for j in i :
      if j == '1' :
        msk += 1
  return msk

def getNetMask(ip):
  return convertMask( ni.ifaddresses( getInterface(ip) )[AF_INET][0]['netmask'] )

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
    #print("checking ",ip)
    if (is_serv(ip)):
      L += [ip]
    ip = ip_inc(ip)
  return L

def calc_plage(IP,mask) :
  IP = IP.split(".")
  maskgroup = mask // 8
  maskrange = mask % 8
  ip_init = ""
  for i in range(maskgroup) : # Creating the net part of the address
    ip_init += str(IP[i])+"."
  ip_last = ip_init #Same net part
  IP_bin_init = bin(int(IP[maskgroup]))[2:] # we convert the IP into binary and we remore the '0b'
  IP_bin_init = "0"*(8-len(IP_bin_init)) + IP_bin_init # we make IP_bin have a len of 8
  
  IP_bin_init = IP_bin_init[:maskrange] + "0" * (8-maskrange)
  IP_bin_last = IP_bin_init[:maskrange] + "1" * (8-maskrange)

  ip_init += str(int(IP_bin_init,2))
  ip_last += str(int(IP_bin_last,2))
  for j in range(4-maskgroup-1) :
    ip_init += ".0"
    ip_last += ".255"
  ip_init = ip_inc(ip_init)
  if(ip_last[-1] != 0):
    ip_last = ip_last[:-1] + str(int(ip_last[-1])-1)
  return ip_init,ip_last

def nb_adr(init,last):
  if(init == last) :
    return 1
  return 1+nb_adr(ip_inc(init),last)

def choose_room():
  ip = getIPaddr()
  subnetmask = getNetMask(ip)
  IP = ip.split(".")
  if(subnetmask==0):
    if(IP[0] == "10"): #from 10.0.0.1 to 10.255.255.254
      ip_init = "10.0.0.1"
      ip_last = "10.255.255.254"
    elif (IP[0] == "172") : #from 172.16.0.1 to 172.31.255.254
      ip_init = "172."+str(IP[1])+".0.1"
      ip_last = "172."+str(IP[1])+".255.254"
    elif (IP[0] == "192") : #from 192.168.0.1 to 192.168.255.254
      ip_init = "192.168."+str(IP[2])+".1"
      ip_last = "192.168."+str(IP[2])+".254"
    else :
      ip_init = "0.0.0.0"
      ip_last = "0.0.0.0"
  else :
    ip_init,ip_last = calc_plage(ip,subnetmask)
  msg = "checking from " + ip_init + " to " + ip_last + " (" + str(nb_adr(ip_init,ip_last)) + " adr)"
  print(msg)
  L = check_rooms(ip_init,ip_last)
  i = 1
  if(len(L) == 0) :
    print("Rooms not found")
    exit()
  for e in L :
    msg = str(i) + " : " + str(e)
    print(msg)
  room = L[int(sys.stdin.readline())-1]
  return room