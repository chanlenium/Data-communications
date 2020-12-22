import socket

# Server address
HOST = '127.0.0.1'
# Port number
PORT = 50003

# Create socket object(address family: IPv4, socket type: TCP).
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Code to resolve WinError 10048
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# bind function to make socket connect network and port number
server_socket.bind((HOST, PORT))

# allow server to connect client
server_socket.listen()

# return a new socket when a client connects
client_socket, addr = server_socket.accept()

# print an address of client
print('Connected by', addr)

while True:

    # standby for receiving message from client
    data = client_socket.recv(1024)

    # Break loop when receiving empty string
    if not data:
        break

    # Print a receiving message
    print('Received from', addr, data.decode())

    # echo message to client
    client_socket.sendall(data)

# close socket
client_socket.close()
server_socket.close()