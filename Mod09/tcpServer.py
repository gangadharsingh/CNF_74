import socket
import random
import threading
from _thread import *
def guess(data, num, client, count):
	# count = count+1
	client1 = client
	if data == num:
		data1 = "Correct, number of guess is ",count
		client1.send(str(data1).encode())
	elif data < num:
		data1 = "Your number is lesser than guess"
		client1.send(str(data1).encode())
	elif data > num:
		data1 = "Your number is higher than guess"
		client1.send(str(data1).encode())

def Main():
	host = socket.gethostname()
	port = 8005
	s = socket.socket()
	s.bind((host,port))
	s.listen(1)
	c, addr = s.accept()
	count = 0
	num = int(random.randint(0, 50))
	print("Connection from: ", str(addr))
	while True:
		data  = c.recv(1024).decode()
		count = count + 1
		print(num, '\n')
		if not data:
			break
		print("from connected user: ", str(data))
		start_new_thread(guess, (int(data), num, c, count))
		# print("sending: ", str(data))
		# c.send(data.encode())
	c.close()

if __name__ == '__main__':
	Main()