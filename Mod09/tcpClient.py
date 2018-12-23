import socket

def Main():
	host = socket.gethostname()
	port = 8005

	s = socket.socket()
	s.connect((host,port))

	message = input("-> ")
	while message != 'q':
		s.send(message.encode())
		data = s.recv(1024).decode()
		print("Recieved from server: ", str(data))
		message = input("-> ")
	s.close()

if __name__ == '__main__':
	Main()