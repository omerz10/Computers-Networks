import socket
import sys
def main():

	server =socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	server_ip ='0.0.0.0'
	server_port =12345
	server.bind((server_ip, server_port))
	while True:
		data, sender_info = server.recvfrom(4096)  
		print 'Received: ', data, 'data len: ', len(data), 'from: ', sender_info
		server.sendto("B",sender_info)
   
   
if __name__ == "__main__":
	main()
	sys.exit(0)
