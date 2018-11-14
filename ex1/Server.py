from socket import socket, AF_INET, SOCK_DGRAM
import sys


def extract_file_data(ipsFileName, data_base):
 """

 :param ipsFileName:
 :return:
 """
 with open(ipsFileName, 'r') as fp:
  lines = fp.read().split("\n")
  for line in lines:
   domain, ip = line.split(",")
   data_base.update({domain : ip})
 fp.close()


def add_to_db(domain, ip, ips_file_name):
    """

    :param domain:
    :return:
    """
    with open(ips_file_name, 'a') as fp:
        line = '\n' + domain + ',' + ip + '\n'
        fp.write(line)
        fp.close()

def start_server(my_port, parent_ip, parent_port, ips_file_name):
 """

 :param myPort:
 :param parentIP:
 :param parentPort:
 :param ipsFileName:
 :return:
 """
 s = socket(AF_INET, SOCK_DGRAM)
 source_ip = '127.0.0.1'
 source_port = my_port
 s.bind((source_ip, int(source_port)))
 data_base = {}
 # extract data from file into data set
 extract_file_data(ips_file_name, data_base)

 while True:
  domain, sender_info = s.recvfrom(2048)
  # domain is in server's data. send result to client
  if domain in data_base:
   s.sendto(data_base[domain], sender_info)

  # send data to master server
  else:
   s.sendto(domain, (parent_ip, int(parent_port)))
   ip, father_info = s.recvfrom(2048)
   add_to_db(domain, ip, ips_file_name)
   s.sendto(ip, sender_info)


if __name__ == "__main__":
 my_port = sys.argv[1]
 parent_ip = sys.argv[2]
 parent_port = sys.argv[3]
 ips_file_name = sys.argv[4]
 start_server(my_port, parent_ip, parent_port, ips_file_name)
 sys.exit()
