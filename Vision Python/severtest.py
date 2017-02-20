import socket

#server
HOST = "127.0.0.1"
PORT = 6969
message = b"test"

sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP

sock.connect((HOST, PORT))
sock.send(message)

