import socket
def Main():
	host = '10.2.138.97'
	port = 8000
	s = socket.socket()
	s.bind((host,port))
	s.listen(1)
	c, addr = s.accept()
	print("Connection from: ", str(addr))
	while True:
		data  = c.recv(1024).decode()
		if not data:
			break
		print("from connected user: ", str(data))
		data = str(data).upper()
		print("sending: ", str(data))
		c.send(data.encode())
	c.close()

if __name__ == '__main__':
	Main()