#!/usr/bin/env python3

import socket
import sys

if (len(sys.argv) < 2):
    print('Usage: Client <server-IP>')
    quit()

HOST = sys.argv[1] # The server's hostname or IP address
PORT = 12345        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_client:
    socket_client.connect((HOST, PORT))
    bytes = input('Insert a new message for the server: ')
    socket_client.sendall(str.encode(bytes))
    data = socket_client.recv(1024)
    data_str = data.decode()
    print('Received:', data_str)
