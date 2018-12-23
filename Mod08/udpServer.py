import socket

def currencyConvt(data):
	inr = 67.0
	pound = 0.75
	yen = 113.41
	data1 = data.split()
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
	host = socket.gethostname()
	port = 8002
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host,port))
	# s.listen(1)
	# c, addr = s.accept()
	print("Server started.")
	while True:
		data, addr  = s.recvfrom(1024)
		# if not data:
		# 	break
		
		# if(data)
		# data = str(data.decode("ASCII")).upper()
		print("sending: "+str(data))
		data = currencyConvt(data.decode())
		print(data)
		s.sendto(str(data).encode("ASCII"), addr)


	s.close()

if __name__ == '__main__':
	Main()