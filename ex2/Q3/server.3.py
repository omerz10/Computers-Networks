from socket import socket, AF_INET, SOCK_STREAM
import sys

import os
os.chdir(os.getcwd() + "/files")

DEFAULT_FILE_PATH = "index.html"
REDIRECT_FILE_PATH = "result.html"

def extract_file(data):
    path = data.split()[1][1:]  # extract second word on browser's message.
    if path == "": path = DEFAULT_FILE_PATH
    if path == "redirect": path = REDIRECT_FILE_PATH
    suffix = path[-3:]
    if os.path.isfile(path):
        if suffix == "jpg" or suffix == "ico":
            file = open(path, 'rb')  # reads pictures in binary.
        else:
            file = open(path, 'r')
        return path, file
    else:
        return path, None


def main():
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_ip = '0.0.0.0'
    server_port = 12345
    server_socket.bind((server_ip, server_port))
    server_socket.listen(5)
    while True:
        client_socket, client_address = server_socket.accept()
        data = client_socket.recv(256)  # chosen file name client expects
        path, file = extract_file(data)
        while (data[-4:] != "\r\n\r\n"):
            data = client_socket.recv(256)  # reads and ignores rest of client's message (known suffix '\r\n\r\n')
        print 'Client requests file: ' + path
        if file is not None:  # chosen file exists on the server
            if path is REDIRECT_FILE_PATH:
                client_socket.send("HTTP/1.1 301 Moved Permanently\n")
                client_socket.send("Connection: close\n")
                client_socket.send("Location: /result.html\n\n")
            else:
                client_socket.send("HTTP/1.1 200 OK\n")
                client_socket.send("Connection: close\n\n")

            l = file.read(1024)
            while (l):
                client_socket.send(l)
                l = file.read(1024)
            file.close()
        else:
            client_socket.send("HTTP/1.1 404 Not Found\n")
            client_socket.send("Connection: close\n\n")
        client_socket.close()


if __name__ == "__main__":
    main()
    sys.exit(0)