from threading import Thread as T
import time
import sys

def func(num: int = 10)-> str:
    if scenario == 3:
        time.sleep(0.2 * num)
    print(f"Function called by thread {num}")

if __name__ == "__main__":
    scenario = int(sys.argv[1])
    n_threads = int(sys.argv[2])

    for i in range(n_threads):
        t = T(target=func, args=(i,))
        t.start()
        if scenario == 1:
            t.join()
        elif scenario == 2:
            time.sleep(0.3)