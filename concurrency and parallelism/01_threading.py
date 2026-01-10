import threading 
import time


def take_orders():
    for i in range (1, 4):
        print (f"Taking order for#{i}")
        time.sleep(1) #this will halt the execution for 1second
        
def make_orders():
    for i in range(1,4):
        print(f"making the orders for{i}")
        time.sleep(2)
        
#create the threads

order_thread= threading.Thread(target=take_orders)
make_thread= threading.Thread(target=make_orders)

order_thread.start()
make_thread.start()

#wait for both to finish
order_thread.join()
make_thread.join()

print(f"All orders taken and made well")