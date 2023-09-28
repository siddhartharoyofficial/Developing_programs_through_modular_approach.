import socket

# Define the server's address and port
server_address = ('<Server1_IP>', <Server1_Port>)

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the server address
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)

print(f"Server 1 listening on {server_address[0]}:{server_address[1]}")

# Accept a connection
client_socket, client_address = server_socket.accept()

# Receive data from the client
data = client_socket.recv(1024)
print(f"Server 1 received: {data.decode()}")

# Send a response back to the client
response = "Hello from Server 1!"
client_socket.send(response.encode())

# Close the sockets
client_socket.close()
server_socket.close()
