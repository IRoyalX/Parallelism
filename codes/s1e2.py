from threading import Thread as T
import time, sys, threading

def FA():
    if scenario == 3:
        time.sleep(0.3)
    print(f"Starting thread {threading.currentThread().getName()}")
    time.sleep(0.3)
    if scenario == 1:
        time.sleep(0.1)
    print(f"Exiting from thread {threading.currentThread().getName()}")

def FB():
    if scenario == 3:
        time.sleep(0.2)
    print(f"Starting function {threading.currentThread().getName()}")
    time.sleep(0.3)
    if scenario == 1:
        time.sleep(0.2)
    print(f"Exiting from function {threading.currentThread().getName()}")

def FC():
    if scenario == 3:
        time.sleep(0.1)
    print(f"Starting function {threading.currentThread().getName()}")
    time.sleep(0.3)
    if scenario == 1:
        time.sleep(0.3)
    print(f"Exiting from function {threading.currentThread().getName()}")

if __name__ == "__main__":
    scenario = int(sys.argv[1])
    n_threads = int(sys.argv[2])

    A = T(target=FA, name= "A")
    B = T(target=FB, name= "B")
    C = T(target=FC, name= "C")
    A.start()
    if scenario == 2:
        A.join()
    B.start()
    if scenario == 2:
        B.join()
    C.start()
    if scenario == 2:
        C.join()