import time, sys, random, threading

def consumer():
 global item
 if not semaphore._value:
    print("Consumer is waiting ...")
 semaphore.acquire()
 print(f"Consumer notify: item number {item}")

def producer():
 global item
 if scenario == 1:
    time.sleep(0.2)
 item = random.randint(0, 1000)
 print(f"Producer notify: item number {item}")
 semaphore.release()

if __name__ == "__main__":
    scenario = int(sys.argv[1])
    n_threads = int(sys.argv[2])

    semaphore = threading.Semaphore(0)
    item = 0
    for i in range(n_threads):
        cons = threading.Thread(target=consumer)
        prod = threading.Thread(target=producer)
        if scenario != 3:
            cons.start()
        prod.start()
        if scenario == 3:
           cons.start()
