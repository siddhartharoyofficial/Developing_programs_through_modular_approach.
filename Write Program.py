# Program 1: Writing to the Named Pipe

import os

# Define the path to the named pipe (FIFO)
pipe_path = "my_named_pipe"

# Check if the named pipe exists; if not, create it
if not os.path.exists(pipe_path):
    os.mkfifo(pipe_path)

# Open the named pipe for writing
with open(pipe_path, "w") as pipe:
    message = "Hello from Program 1!"
    pipe.write(message)
    print(f"Program 1 wrote: {message}")