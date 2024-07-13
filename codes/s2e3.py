import multiprocessing
import time, sys

def func():
    name = multiprocessing.current_process().name
    print (f"Starting {name}\n")
    time.sleep(0.1)
    if name == 'background_process':
        for i in range(0, 10, 2):
            print(f"---> {i}\n")
            time.sleep(0.2)
    else:
        for i in range(1, 10, 2):
            print(f"---> {i}\n")
            time.sleep(0.2)
    time.sleep(0.1)
    print (f"Exiting {name}\n")

if __name__ == "__main__":
    scenario = int(sys.argv[1])

    background_process = multiprocessing.Process(name="background_process",target=func)
    if scenario != 2:
        background_process.daemon = True
    NO_background_process = multiprocessing.Process(name="NO_background_process",target=func)
    NO_background_process.daemon = False
    background_process.start()
    if scenario == 3:
        background_process.join()
    NO_background_process.start()
