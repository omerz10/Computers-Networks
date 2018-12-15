import socket
import sys
def main():

	server =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server_ip ='0.0.0.0'
	server_port =12345
	server.bind((server_ip, server_port))
	server.listen(5)
	while True:
		client_socket, client_address = server.accept()
		counter = 0
		print 'Connection from: ', client_address
		data = client_socket.recv(1024)  #  recv first segment
		counter += len(data)
		print 'Client sent: ',data
		while counter < 22:
			data = client_socket.recv(1024)
			counter += len(data)
			print 'Received: ', data, 'data len: ', len(data)
		client_socket.send("B")
		client_socket.close()
   
   
if __name__ == "__main__":
	main()
	sys.exit(0)
