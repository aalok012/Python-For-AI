import threading
import time

def monitor_temp():
    while True:
        print(f"Montoring temp")
        time.sleep(2)
        
t= threading.Thread(target= monitor_temp, daemon=True)# remove daemon for non daemon thread
t.start()

print(f"Main program done")