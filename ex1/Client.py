from socket import socket, AF_INET, SOCK_DGRAM
import sys

def start_client(server_ip, server_port):

 s = socket(AF_INET, SOCK_DGRAM)
 dest_ip = server_ip
 dest_port = server_port
 domain = raw_input("Please insert domain: ")
 while not domain == 'quit':
  s.sendto(domain, (dest_ip,int(dest_port)))
  data, sender_info = s.recvfrom(2048)
  print data
  domain = raw_input("Please insert domain: ")
 s.close()



if __name__ == "__main__":
 server_ip, server_port = sys.argv[1:]
 start_client(server_ip, server_port)