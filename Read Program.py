import os

# Define the path to the named pipe (FIFO)
pipe_path = "my_named_pipe"

# Open the named pipe for reading
with open(pipe_path, "r") as pipe:
    message = pipe.read()
    print(f"Program 2 received: {message}")