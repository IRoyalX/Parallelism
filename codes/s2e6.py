import multiprocessing
import time, sys, random

class producer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue
    def run(self, n_products) :
        for _ in range(n_products):
            item = random.randint(0, 256)
            self.queue.put(item)
            print ("Process Producer : item %d appended to queue %s" % (item,self.name))
            time.sleep(1)
            print ("The size of queue is %s" % self.queue.qsize())

class consumer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue
    def run(self):
        while True:
            if (self.queue.empty()):
                print("the queue is empty")
                break
            else :
                time.sleep(2)
                item = self.queue.get()
                print ('Process Consumer : item %d popped from by %s \n' % (item, self.name))
                time.sleep(1)

if __name__ == '__main__':
    scenario = int(sys.argv[1])
    n_products = int(sys.argv[2])

    queue = multiprocessing.Queue()
    process_producer = producer(queue, n_products)
    process_consumer = consumer(queue)
    process_producer.start()
    process_consumer.start()
    process_producer.join()
    process_consumer.join()