import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = (sys.argv[1], int(sys.argv[2]))

print(server_address)
sock.bind(server_address)

sock.listen(3)

connection, client_address = sock.accept()

while True:
    data = connection.recv(1024*1024)
