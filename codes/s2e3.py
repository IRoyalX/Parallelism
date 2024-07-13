from multiprocessing import Queue
import multiprocessing
import time, sys

def func(output):
    name = multiprocessing.current_process().name
    output.put(f"Starting {name}\n")
    time.sleep(0.1)
    if name == 'background_process':
        for i in range(0, 10, 2):
            output.put(f"---> {i}\n")
            time.sleep(0.2)
    else:
        for i in range(1, 10, 2):
            output.put(f"---> {i}\n")
            time.sleep(0.2)
    time.sleep(0.1)
    output.put(f"Exiting {name}\n")

if __name__ == "__main__":
    scenario = int(sys.argv[1])
    output = Queue()

    background_process = multiprocessing.Process(name="background_process", target=func, args=(output, ))
    if scenario != 2:
        background_process.daemon = True
    NO_background_process = multiprocessing.Process(name="NO_background_process", target=func, args=(output, ))
    NO_background_process.daemon = False
    background_process.start()
    if scenario == 3:
        background_process.join()
    NO_background_process.start()

    background_process.join()
    NO_background_process.join()
    while not output.empty():
        print(output.get())
