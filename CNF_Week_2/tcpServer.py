import socket
# from xlrd import open_workbook
import threading
from _thread import *

def attendance(data, secret_QandA, client):
	msg = "ATTENDANCE-FAILURE"
	data1 = data.split()
	try:
		if data1[0] == "MARK-ATTENDANCE":
			if secret_QandA.contains(data1[1]):
				# print("ATTENDANCE SUCCESS")
				client.send("ATTENDANCE SUCCESS".encode())
				# client.send("q".encode())
			else:
				client.send("ROLLNUMBER-NOTFOUND".encode())
				while msg == "ATTENDANCE-FAILURE":
					message = "SECRETQUESTION-" + secret_QandA[data1[1]][1]
					client.send(message.encode())
					newdata  = client.recv(1024).decode()
					if str(newdata.decode()) == secret_QandA[data1[1]][2]:
						msg = "ATTENDANCE SUCCESS"
						client.send("ATTENDANCE SUCCESS".encode())
						client.close()
					else:
						client.send("ATTENDANCE-FAILURE".encode())
					if str(newdata.decode()) == 'q':
						client.send("q".encode())
						client.close()
						break
	except:
		client.send("q".encode())
		client.close()

def Main():
	host = socket.gethostbyname((socket.gethostname()))
	port = 8001
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((host,port))
	s.listen(5)
	c, addr = s.accept()
	print("Connection from: ", str(addr))
	# student = open_workbook('data.xls')
	secret_QandA = {}
	# store student question and answer in a dictionary
	# for std in student.sheets():
	# 	row = sheet.nrows
	# 	for r in range(row):
			# secret_QandA[sheet.cell_value(r,0)] = [sheet.cell_value(r, 1), sheet.cell_value(r, 2)]
	secret_QandA = {20158501:["What is my first vehicle first number?","501"],
					20158502:["What is my masters degree?","MSIT"],
					20158503:["Who is my close friend?","Sriram"],
					20158504:["When did you meet your close friend?","1999"],
					20158505:["What’s your mother's maiden name?","John"],
					20158506:["Who invented telephone?","Graham Bell"],
					20158507:["Who invented radium?","Madam Curie"],
					20158508:["Which country is called as land of rising sun?","Japan"],
					20158509:["Which country is called of white elephants?","Thailand"],
					20158510:["Gateway of India?","Mumbai"]}
	while True:
		data  = c.recv(1024)
		if not data:
			break
		print("from connected user: ", str(data.decode()))
		start_new_thread(attendance, (data,secret_QandA, c))
		# print("sending: ", str(data))
		# c.send(data.encode())
	c.close()

if __name__ == '__main__':
	Main()