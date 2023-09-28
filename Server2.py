import socket

# Define the server's address and port
server_address = ('<Server2_IP>', <Server2_Port>)

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the remote server
server_socket.connect(server_address)

# Send data to the server
message = "Hello from Server 2!"
server_socket.send(message.encode())

# Receive a response from the server
response = server_socket.recv(1024)
print(f"Server 2 received: {response.decode()}")

# Close the socket
server_socket.close()
