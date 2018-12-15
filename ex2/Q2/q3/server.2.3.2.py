import socket
import sys
def main():

	server =socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	server_ip ='0.0.0.0'
	server_port =12345
	server.bind((server_ip, server_port))
	counter = 0
	while counter <22:
		data, sender_info = server.recvfrom(1024)  
		counter +=len(data)
		print 'Client sent: ' , data
	
	server.sendto("B",sender_info)
	server.close()
   
   
if __name__ == "__main__":
	main()
	sys.exit(0)
