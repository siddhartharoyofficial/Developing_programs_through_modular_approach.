#Program 2: Receiving Data from Message Queue

import multiprocessing

# Function for receiving data from the message queue
def receiver(queue):
    message = queue.get()
    print(f"Program 2 received: {message}")

if __name__ == "__main__":
    # Create a message queue
    message_queue = multiprocessing.Queue()
    
    # Start the receiver process
    receiver_process = multiprocessing.Process(target=receiver, args=(message_queue,))
    receiver_process.start()
    receiver_process.join()  # Wait for the receiver process to finish

    # Close the message queue
    message_queue.close()
    message_queue.join_thread()
