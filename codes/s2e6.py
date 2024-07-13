from multiprocessing import Queue
import multiprocessing
import time, sys, random

class producer(multiprocessing.Process):
    def __init__(self, queue, n_products, scenario, output):
        multiprocessing.Process.__init__(self)
        self.queue = queue
        self.n_products = n_products
        self.scenario = scenario
        self.output = output
    def run(self) :
        for _ in range(self.n_products):
            item = random.randint(0, 256)
            self.queue.put(item)
            if self.scenario != 3:
                time.sleep(0.2)
            self.output.put(f"Producer : {item} appended to Q")
            self.output.put(f"The size of Q is {self.queue.qsize()}\n")
            
class consumer(multiprocessing.Process):
    def __init__(self, queue, scenario, output):
        multiprocessing.Process.__init__(self)
        self.queue = queue
        self.scenario = scenario
        self.output = output
    def run(self):
        while True:
            if (self.queue.empty()):
                self.output.put("The Q is empty")
                break
            else :
                if self.scenario == 1:
                    time.sleep(0.4)
                item = self.queue.get()
                self.output.put(f"Consumer : {item} popped from Q\n")

if __name__ == "__main__":
    scenario = int(sys.argv[1])
    n_products = int(sys.argv[2])
    output = Queue()

    queue = Queue()
    p = producer(queue, n_products, scenario, output)
    c = consumer(queue, scenario, output)
    p.start()
    c.start()

    p.join()
    c.join()
    while not output.empty():
        print(output.get())
