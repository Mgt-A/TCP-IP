#!/usr/bin/env python

import websocket
import sys

# Get the command
cmd = sys.argv[1]

on_message_counter = 0

# Called when the Websockets app receives a message
def on_message(ws, message):
    global on_message_counter
    on_message_counter +=1
    print(message.decode())


# Called on connection's opening
def on_open(ws):
    ws.send(cmd)

# Create a websocket app with the appropriate callbacks
ws = websocket.WebSocketApp('ws://tcpip.epfl.ch:5006',
                          on_message = on_message,
                          on_open    = on_open)
ws.run_forever()
print()
print("on_message was called %d times" % on_message_counter)
