## Semaphore

# A semaphore limits how many threads can access a resource simultaneously.

# Example


import threading
import time

sem = threading.Semaphore(2)

def worker(name):
    with sem:
        print(name, "Working")
        time.sleep(2)

for i in range(5):
    threading.Thread(target=worker,args=(i,)).start()
    
    
