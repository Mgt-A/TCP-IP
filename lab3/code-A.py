import socket

HOST = 'localhost' # The remote host
PORT = 5001 #port number of communicating partner

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(b'Hello, Romeo ', (HOST,PORT))
s.close()
print('Message sent')
