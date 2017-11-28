#!/usr/bin/env python3

import socket
import struct

RECV_SIZE = 1024

HOST = '224.1.1.1' # The remote host
PORT = 5005        # port number of communicating partner

socket_type = socket.AF_INET

# use SOCK_DGRAM for UDP
s = socket.socket(socket_type, socket.SOCK_DGRAM)
# SO_REUSEADDR
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind to port 5005
s.bind(('', PORT))


# Special options
# ---------------
# `=`  means "use platform endianess"
# `4s` means "first thing is a string of four chars"
# `l`  means "a long integer follows"
mreq = struct.pack("4sl", socket.inet_aton(HOST), socket.INADDR_ANY)
# Need to say that we are interested in this multicast (http://www.tldp.org/HOWTO/Multicast-HOWTO-6.html)
s.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

# Receive the data
while True:
    data = s.recv(RECV_SIZE)
    uid, msg = data[0:6].decode(), data[6:].decode()
    print(msg)
