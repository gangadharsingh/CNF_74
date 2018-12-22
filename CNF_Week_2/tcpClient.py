import socket

def Main():
	host = socket.gethostname()
	port = 8001

	s = socket.socket()
	s.connect((host,port))
	print("Syntax: MARK-ATTENDANCE ROLLNUMBER")
	message = input("-> ")
	while message != 'q':
		s.send(message.encode())
		data = s.recv(1024).decode()
		print("Recieved from server: ", str(data))
		if str(data) == "SECRETQUESTION":
			print("Syntax: SECRETANSWER Answeritself")
			response = input()
			s.send(response.encode())
		elif str(data) == "ATTENDANCE-SUCCESS":
			break
		elif str(data) == "q":
			break
		message = input("-> ")
	s.close()

if __name__ == '__main__':
	Main()