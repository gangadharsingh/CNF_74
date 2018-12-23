import socket
def Main():
	host = socket.gethostname()
	port = 8001
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host,port))
	# s.listen(1)
	# c, addr = s.accept()
	print("Server started.")
	while True:
		data, addr  = s.recvfrom(1024)
		# if not data:
		# 	break
		print("message from: " +str(addr))
		print("from connect user: "+str(data.decode()))
		data = str(data.decode("ASCII")).upper()
		print("sending: "+str(data))
		s.sendto(data.encode("ASCII"), addr)
	s.close()

if __name__ == '__main__':
	Main()