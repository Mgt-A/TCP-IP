#!/usr/bin/env python3

import socket
import fileinput

HOST = '224.1.1.1' # Multicast host
PORT = 5005        # port number of communicating partner

UID = '224797' # SCIPER
socket_type = socket.AF_INET

# Use SOCK_DGRAM for UDP
s = socket.socket(socket_type, socket.SOCK_DGRAM)

# Read text form stdin
for line in fileinput.input():
    msg = UID + line
    s.sendto(msg.encode(), (HOST, PORT))
