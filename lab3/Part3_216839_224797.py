#!/usr/bin/env python3

import socket
import datetime
import numpy as np

# Constants (Utility, used for indexing)
IPv4 = 0
IPv6 = 1

# Arbitrary read length
RECV_READ_LEN = 32

HOST = 'lab3.iew.epfl.ch' # The remote host
PORT = 5004 #port number of communicating partner

# Configuration of the sockets
socket_types = [socket.AF_INET, socket.AF_INET6] # Possible socket types
type_str = ['AF_INET', 'AF_INET6']               # Socket type strings for __repr__
socket_type = IPv4                               # Try IPv4 first

class Logger:
    '''
    Records relevant information, used to print information about the run.
    '''
    def __init__(self):
        self.successfulPackets = 0 # Number of succesful packets
        self.timeOuts = 0          # Number of successive timeouts
        self.totalPackets = 0      # Total number of packets in this run
        self.packetToSuccess = []  # Records number of timeouts before a succesful packet arrives

    def resetTimeOutCounter(self):
        self.timeOuts = 0

# Initialize the logger
l = Logger()

# Run until we get 60 successful packets
while l.successfulPackets < 60:
    l.totalPackets += 1
    try:
        # Create the socket
        s = socket.socket(socket_types[socket_type], socket.SOCK_DGRAM)
        s.settimeout(1)

        # Send the command
        s.sendto(b'RESET:20', (HOST,PORT))

        # Try to read response
        data = s.recv(RECV_READ_LEN)

        s.close()

        # Log attempt
        l.successfulPackets += 1
        l.packetToSuccess.append(l.timeOuts)
        l.resetTimeOutCounter()

        # Print the acquired information
        # Format :
        #   if success :
        #       [Timestamp] - Response
        #   else
        #       timed out
        print('{} - connecting to {}'.format(datetime.datetime.now(), type_str[socket_type]))
        print(data.decode())

    except OSError as e:
        l.timeOuts += 1
        print(e)
        # after a failed attempt, switch between IPv4 and Ipv6
        socket_type = (socket_type + 1) % len(socket_types)
        s.close()

# Print some metrics about run
print("Run result ----")
print(np.mean(l.packetToSuccess)) # Average number of packets before success
print(1.0 - float(l.successfulPackets)/l.totalPackets) # Error ratio
