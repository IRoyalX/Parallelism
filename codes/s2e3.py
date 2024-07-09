import multiprocessing
import time, sys

def foo():
    name = multiprocessing.current_process().name
    print (f"Starting {name}\n")
    if name == 'background_process':
        for i in range(0,5):
            print(f"---> {i}\n")
            time.sleep(1)
    else:
        for i in range(5,10):
            print(f"---> {i}\n")
            time.sleep(1)
    print (f"Exiting {name}\n")

if __name__ == '__main__':
    scenario = int(sys.argv[1])

    background_process = multiprocessing.Process(name='background_process',target=foo)
    background_process.daemon = True
    NO_background_process = multiprocessing.Process(name='NO_background_process',target=foo)
    NO_background_process.daemon = False
    background_process.start()
    NO_background_process.start()
