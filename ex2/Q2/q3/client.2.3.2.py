import socket,sys,time

def main():
	s =socket.socket(socket.AF_INET,socket.SOCK_DGRAM)	
	dest_ip = '192.168.1.125'
	dest_port = 12345
	s.connect((dest_ip,dest_port))
	
	msg ="A"
	s.sendto(msg,(dest_ip,dest_port))
	s.sendto(msg,(dest_ip,dest_port))
	time.sleep(2)
	for i in range(10):
		s.sendto(msg,(dest_ip,dest_port))
		s.sendto(msg,(dest_ip,dest_port))
	data,sender_info = s.recvfrom(4096)
	print "Server sent: ", data
	s.close()
	
if __name__ == "__main__":
	main()
	sys.exit(0)