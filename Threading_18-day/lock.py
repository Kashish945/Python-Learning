# Synchronization issue in threading

import threading
balance=200

lock=threading.Lock()

def deposit(amount, times):
    global balance
    
    for _ in range(times):
        lock.acquire()
        balance +=amount # Critical Section
        lock.release()
  
def withdraw(amount, times):
      global balance
      
      for _ in range(times):
          lock.acquire()
          balance -=amount # Critical Section
          lock.release()
   
deposit_thread = threading.Thread(target=deposit,args=[1,10000])
withdraw_threaad= threading.Thread(target=withdraw,args=[1,10000])

deposit_thread.start()
withdraw_threaad.start()

deposit_thread.join()
withdraw_threaad.join()

print("Final Balance",balance)