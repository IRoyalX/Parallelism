
from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep
import sys

def runner(num):
    global runners, finish_line
    if scenario == 1:
        sleep(randrange(3, 5))
    elif scenario ==2:
        sleep((num + 1) * randrange(1, 3))
    elif scenario == 3:
        sleep(num + 1)
    print(f"'{runners.pop()}' reached the barrier:\n--> {ctime()} \n")
    finish_line.wait()
 
def Fmain():
    global runners, threads
    print('START RACE!!!!\n')
    for i in range(len(runners)):
        threads.append(Thread(target=runner, args=(i, )))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('RACE OVER!')

if __name__ == "__main__":
    scenario = int(sys.argv[1])

    runners = ['Reza', 'Ali', 'Hassan']
    finish_line = Barrier(len(runners))
    threads = []
    Fmain()