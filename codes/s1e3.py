from threading import Thread as T
from random import randint
import time, sys, os 

class SubClass(T):
    def __init__(self, name, duration):
        T.__init__(self)
        self.name = name
        self.duration = duration

    def run(self):
        print (f"{self.name} running, process ID {str(os.getpid())}")
        time.sleep(self.duration)
        print (f"{self.name} over")

if __name__ == "__main__":
    scenario = int(sys.argv[1])
    n_threads = int(sys.argv[2])

    start_time = time.time()

    threads = []
    for i in range(1, n_threads):
        if scenario == 1:
            duration = randint(1,3)
        elif scenario == 2:
            duration = 0
        elif scenario == 3:
            duration = 0.001
        thread = SubClass(f"Thread {i}", duration)
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()   

    print(f"\n-- {(time.time() - start_time)} seconds --\n")