import socket

def getIPaddr():
  try :
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("gmail.com",80))
    ip = s.getsockname()[0]
    s.close()
  except Exception :
    p = "INTERNET NOT TWERKING"
    print(p)
  finally :
    return ip