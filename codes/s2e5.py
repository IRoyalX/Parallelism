from multiprocessing import Queue
import multiprocessing, sys, time

class MyClass(multiprocessing.Process):
    def __init__(self, output):
        multiprocessing.Process.__init__(self)
        self.output = output
    def run(self):
        time.sleep(0.5)
        self.output.put(f"called run method by {self.name}")

if __name__ == "__main__":
    scenario = int(sys.argv[1])
    n_process = int(sys.argv[2])
    output = Queue()

    processes = []
    for i in range(n_process):
        process = MyClass(output)
        processes.append(process)
        process.start()
        if scenario == 1:
            process.join()
        elif scenario == 3 and i%2 == 0:
            process.join()
            
    for process in processes:
        process.join()
    while not output.empty():
        print(output.get())