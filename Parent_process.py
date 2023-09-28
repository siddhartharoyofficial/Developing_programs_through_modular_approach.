# Case Study 


# Write a pipe based communication between process and its child.
import os
import sys

# Create a pipe
parent_pipe, child_pipe = os.pipe()

# Fork a child process
child_pid = os.fork()

if child_pid == 0:  # Child process
    # Close the write end of the pipe in the child process
    os.close(parent_pipe)
    
    # Read data from the pipe
    data = os.read(child_pipe, 100)
    
    # Print the received message
    print(f"Child Process ({os.getpid()}): Received message from Parent: {data.decode()}")
    
    # Close the read end of the pipe in the child process
    os.close(child_pipe)
    
else:  # Parent process
    # Close the read end of the pipe in the parent process
    os.close(child_pipe)
    
    message = "Hello, Child!"
    
    # Write data to the pipe
    os.write(parent_pipe, message.encode())
    
    # Close the write end of the pipe in the parent process
    os.close(parent_pipe)
    
    print(f"Parent Process ({os.getpid()}): Sent message to Child: {message}")

