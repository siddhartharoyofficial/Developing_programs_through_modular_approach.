#Program 1: Sending Data to Message Queue

import multiprocessing

# Function for sending data to the message queue
def sender(queue):
    message = "Hello from Program 1!"
    queue.put(message)
    print(f"Program 1 sent: {message}")

if __name__ == "__main__":
    # Create a message queue
    message_queue = multiprocessing.Queue()
    
    # Start the sender process
    sender_process = multiprocessing.Process(target=sender, args=(message_queue,))
    sender_process.start()
    sender_process.join()  # Wait for the sender process to finish

    # Close the message queue
    message_queue.close()
    message_queue.join_thread()
