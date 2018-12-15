import socket,sys,time

def main():
	s =socket.socket(socket.AF_INET,socket.SOCK_STREAM)	
	dest_ip = '192.168.1.125'
	dest_port = 12345
	s.connect((dest_ip,dest_port))
	
	msg ="A"
	s.send(msg)
	s.send(msg)
	for i in range(10):
		s.send(msg)
		s.send(msg)
	data = s.recv(1024)
	print "Server sent: ", data
	s.close()
	
if __name__ == "__main__":
	main()
	sys.exit(0)
