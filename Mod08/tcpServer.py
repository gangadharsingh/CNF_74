import socket
def currencyConvt(data):
	inr = 67.0
	pound = 0.75
	yen = 113.41
	data1 = data.split(' ')
	if data1[1] == 'INR':
		if data1[4] == 'Dollar':
			return (int (data1[2]))/inr
		elif data1[4] == 'Pound':
			return (pound * (int (data1[2])))/inr
		elif data1[4] == 'Yen':
			return (yen * (int (data1[2])))/inr
	if data1[1] == 'Dollar':
		if data1[4] == 'INR':
			return (int (data1[2]))*inr
		elif data1[4] == 'Pound':
			return (int (data1[2]))*pound
		elif data1[4] == 'Yen':
			return (int (data1[2]))*yen
	if data1[1] == 'Pound':
		if data1[4] == 'Dollar':
			return (int (data1[2]))/pound
		elif data1[4] == 'INR':
			return (inr * (int (data1[2])))/pound
		elif data1[4] == 'Yen':
			return (yen * (int (data1[2])))/pound
	if data1[1] == 'Yen':
		if data1[4] == 'Dollar':
			return (int (data1[2]))/yen
		elif data1[4] == 'Pound':
			return (pound * (int (data1[2])))/yen
		elif data1[4] == 'INR':
			return (inr * (int (data1[2])))/yen

def Main():
	host = socket.gethostbyname(socket.gethostname())
	port = 8002
	s = socket.socket()
	s.bind((host,port))
	s.listen(5)
	c, addr = s.accept()
	print("Connection from: ", str(addr))
	while True:
		data  = c.recv(1024).decode('ASCII')
		if not data:
			break
		print("from connected user: ", str(data))
		data = currencyConvt(data)
		print("sending: ", str(data))
		c.send(str(data).encode('ASCII'))
	c.close()

if __name__ == '__main__':
	Main()