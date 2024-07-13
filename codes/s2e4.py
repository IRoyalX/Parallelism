import multiprocessing
import time, sys

def func():
    print ("Starting function\n")
    for i in range(10):
        print(f"--> {i}\n")
        time.sleep(0.2)
    print ("Finished function")

if __name__ == "__main__":
    scenario = int(sys.argv[1])

    p = multiprocessing.Process(target=func)
    print ("Process before execution:", p.is_alive())
    p.start()
    if scenario == 2:
        time.sleep(1)
    print ("Process running:", p.is_alive())
    p.terminate()
    if scenario == 3:
        time.sleep(1)
    print ("Process terminated:", p.is_alive())
    p.join()
    print ("Process joined:", p.is_alive())

    print ("Process exit code:", p.exitcode)