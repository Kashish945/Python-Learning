## Event 
# Used for communication between threads

# example
import threading
import time

event = threading.Event()

def waiter():
    print("Waiting...")
    event.wait()
    print("Started")

def starter():
    time.sleep(3)
    event.set()

threading.Thread(target=waiter).start()
threading.Thread(target=starter).start()


