#   Multiprocessing creates separate, independent Python processes that run simultaneously on different CPU cores. 
# Each process has its own memory space.

from multiprocessing import Process
import time

def make_order(name):
    print(f"Start of {name} making orders")
    time.sleep(3)
    print(f"End of {name} making orders")
    
if __name__ == "__main__":
    order_makers = [
        Process ( target= make_order, args= (f"Order Maker #{i+1}", ))
        for i in range(3)
        
    ]
    
    #start all process 
    for p in order_makers:
        p.start()
    
    #wait for all to complete
    for p in order_makers:
        p.join()
    
    print("All orders served")