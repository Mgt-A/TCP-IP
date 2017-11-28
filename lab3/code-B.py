import socket

HOST = '' # Symbolic name meaning all available interfaces
PORT = 5001 # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))
while True:
    data, addr = s.recvfrom(1024)
    print('Received data: ', data.decode())
    print('From Address: ', addr)
