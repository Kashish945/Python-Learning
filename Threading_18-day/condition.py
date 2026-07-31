## Condition 

# consition allow thred notifies it that a specific condition is true

#example

import threading
import time

condition = threading.Condition()
items = []

def producer():
    for i in range(5):
        time.sleep(1)

        with condition:
            items.append(i)
            print("Produced:", i)
            condition.notify()

def consumer():
    for _ in range(5):

        with condition:
            while not items:
                condition.wait()

            item = items.pop(0)
            print("Consumed:", item)

t1 = threading.Thread(target=consumer)
t2 = threading.Thread(target=producer)

t1.start()
t2.start()

t1.join()
t2.join()