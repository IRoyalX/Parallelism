from multiprocessing import Queue
import multiprocessing
import time, sys

def func(output):
    output.put("Starting function\n")
    for i in range(10):
        output.put(f"--> {i}\n")
        time.sleep(0.2)
    output.put("Finished function")

if __name__ == "__main__":
    scenario = int(sys.argv[1])
    output = Queue()

    p = multiprocessing.Process(target=func, args=(output, ))
    output.put(f"Process before execution: {p.is_alive()}")
    p.start()
    if scenario == 2:
        time.sleep(1)
    output.put(f"Process running: {p.is_alive()}")
    p.terminate()
    if scenario == 3:
        time.sleep(1)
    output.put(f"Process terminated: {p.is_alive()}")
    p.join()
    output.put(f"Process joined: {p.is_alive()}")

    output.put(f"Process exit code: {p.exitcode}")

    while not output.empty():
        print(output.get())