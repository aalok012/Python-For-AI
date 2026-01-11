from multiprocessing import Process, Queue

def prepare_order(queue):
    queue.put("Order is prepared")

if __name__ == "__main__":
    queue = Queue()

    p= Process(target=prepare_order, args=(queue, ))
    p.start()
    p.join()
    print(queue.get())
