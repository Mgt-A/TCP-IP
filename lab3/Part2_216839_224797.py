import socket
import sys

HOST = 'tcpip.epfl.ch' # The remote host
PORT = 5003            # port number of communicating partner

socket_type = socket.AF_INET # IPv4

# Manually got the length of the messages for each d
MSG0_BYTELEN = 18 # length of first message in bytes
MSG0_LEN = 67  # d = 0
MSG1_LEN = 175 # d = 1
BIG_REC  = 1024 # value for large messages

def read_loop(s, size):
    '''
    Read data from socket until the data runs out.
    Prints the data on stdout.
    Returns the number of times recv() was called
    '''
    iterations = 0
    while True:
        iterations +=1
        data = s.recv(MSG1_LEN).decode()
        if data:
            print(data)
        else:
            break
    return iterations

def cmd_short(s, cmd):
    '''
    Send the command `CMD_short:d` to the server
    print the response
    '''
    try:
        # Interpret the command
        d = int(cmd.split(':')[1])
        # Create the message to be sent
        message = cmd.encode()
        s.sendall(message, ) # Send it

        read_len = MSG1_LEN if d else MSG0_LEN
        iters = read_loop(s, read_len)

    except OSError as e:
        print(e)

def cmd_floodme(s):
    '''
    Sends the `CMD_floodme` command.
    prints the response.
    prints the number of times recv() was called
    '''
    s.sendall('CMD_floodme'.encode(),) # Send message
    iters = read_loop(s, BIG_REC)
    print(iters)

if __name__ == '__main__':
    # Create the connection
    s = socket.socket(socket_type, socket.SOCK_STREAM)
    s.connect((HOST,PORT))

    # Parse the desired command
    cmd = sys.argv[1]

    # Dispatch to appropriate responder
    if cmd == 'CMD_floodme':
        cmd_floodme(s)
    elif cmd.split(':')[0] == 'CMD_short':
        cmd_short(s, cmd)
    else:
        print("ERROR -- Coudn't parse command.")
        exit(1)

    s.close()
