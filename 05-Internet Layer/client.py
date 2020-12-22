import socket

# Server address
HOST = '127.0.0.1'
# Port Number
PORT = 50003

# Create socket object(address family: IPv4, socket type: TCP).
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect server
client_socket.connect((HOST, PORT))

# Send a message
client_socket.sendall('Hello, DongchanOh'.encode())

# Receive a message.
data = client_socket.recv(1024)
print('Received', repr(data.decode()))

# Close socket
client_socket.close()