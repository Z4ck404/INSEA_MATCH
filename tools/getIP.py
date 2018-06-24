import socket

try :
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("gmail.com",80))
	print "IP:"+s.getsockname()[0]
	s.close()
except Exception :
	p = "INTERNET NOT TWERKING"
	print p