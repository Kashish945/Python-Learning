## Threading and MultiThreading in Python

# what is Thread ? =>  A Thread is the smallest unit of execution inside a process. A process can contain one or more threads. Threads within the same process share memory and resources.Each thread executes a specific task independently.

# What is Threading? => Threading is the technique of creating and managing multiple threads inside a single process. Instead of doing one task after another, multiple threads execute concurrently. Python provides the threading module to work with threads.

# What is MultiTheading? => Multithreading is the execution of multiple threads simultaneously (or concurrently) within the same process. Each thread performs a different task.

# why need MUltiThreading? 
# Without multithreading, a program performs only one task at a time.
# This causes : Slow execution,CPU waiting,Poor user experience
# Multithreading helps improve responsiveness.


from time import sleep,time
import threading

start_time=time()
def something(id):
    print(f"Going to sleep...{id}")
    sleep(1)
    print(f"Broken up...{id}")
 
threads=[threading.Thread(target=something,args=[1]) for i in range(10)]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

end_time=time()

print(f"Main Thread ended in {end_time-start_time}seconds")


