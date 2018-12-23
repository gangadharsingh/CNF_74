import socket

def Main():
	host = socket.gethostname()
	port = 8002

	server = (socket.gethostname(), 8002)

	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	# s.bind((host,port))

	message = input("-> ")
	while message != 'q':
		s.sendto(message.encode(), server)
		data, addr = s.recvfrom(1024)
		print("Recieved from server: "+ str(data.decode()))
		message = input("-> ")
	s.close()

if __name__ == '__main__':
	Main()