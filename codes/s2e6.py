import multiprocessing
import time, sys, random

class producer(multiprocessing.Process):
    def __init__(self, queue, n_products, scenario):
        multiprocessing.Process.__init__(self)
        self.queue = queue
        self.n_products = n_products
        self.scenario = scenario
    def run(self) :
        for _ in range(self.n_products):
            item = random.randint(0, 256)
            self.queue.put(item)
            if self.scenario != 3:
                time.sleep(0.2)
            print (f"Producer : {item} appended to Q")
            print (f"The size of Q is {self.queue.qsize()}\n")
            

class consumer(multiprocessing.Process):
    def __init__(self, queue, scenario):
        multiprocessing.Process.__init__(self)
        self.queue = queue
        self.scenario = scenario
    def run(self):
        while True:
            if (self.queue.empty()):
                print("The Q is empty")
                break
            else :
                if self.scenario == 1:
                    time.sleep(0.4)
                item = self.queue.get()
                print (f"Consumer : {item} popped from Q\n")

if __name__ == "__main__":
    scenario = int(sys.argv[1])
    n_products = int(sys.argv[2])

    queue = multiprocessing.Queue()
    producer(queue, n_products, scenario).start()
    consumer(queue, scenario).start()
