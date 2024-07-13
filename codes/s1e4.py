from threading import Thread as T
import time, sys, os, threading

class SubClass(T):
    def __init__(self, name, duration):
        T.__init__(self)
        self.name = name
        self.duration = duration

    def run(self):
        if scenario == 3:
            print (f"{self.name} running, process ID {str(os.getpid())}")
            time.sleep(self.duration)
            print (f"{self.name} over")
        else:  
            with Lock:
                print (f"{self.name} running, process ID {str(os.getpid())}")
                time.sleep(self.duration)
                print (f"{self.name} over")

if __name__ == "__main__":
    scenario = int(sys.argv[1])
    n_threads = int(sys.argv[2])
    
    start_time = time.time()
    Lock = threading.Lock()

    threads = []
    for i in range(1, n_threads):
        if scenario != 2:
            duration = 0.5
        elif scenario == 2:
            duration = 0
        thread = SubClass(f"Thread {i}", duration)
        threads.append(thread)
        thread.start()
        if scenario == 3:
            thread.join()
    for i in threads:
        thread.join()

    print(f"\n--- {(time.time() - start_time)} seconds ---")