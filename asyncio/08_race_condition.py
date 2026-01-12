import threading

food_stock =0

def restock():
    global food_stock
    for _ in range (100000):
        food_stock+=1
        
threads= [threading.Thread(target=restock)for _ in range(2)]

for t in threads: t.start()
for t in threads: t.join()


print("food Stock: ", food_stock)