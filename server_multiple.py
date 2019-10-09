#!/usr/bin/env python3

import socket
import sys
from _thread import *

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 12345        # Port to listen on (non-privileged ports are > 1023)


def handler_thread(conn, addr):
    flag_connection = True;
    while (flag_connection):
        print('Connected by', addr)
        data = conn.recv(1024)
        data_str = data.decode()
        print('Received:', data_str)
        bytes = input('Insert a new message for the client: ')
        conn.sendall(str.encode(bytes))
        flag_connection = False
    conn.close()
    print('Disconnected from:', addr)


def Main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    flag = True;
    while (flag):
        print('I am the server')
        conn, addr = server_socket.accept()
        start_new_thread(handler_thread, (conn, addr))

if __name__ == '__main__':
    Main()
