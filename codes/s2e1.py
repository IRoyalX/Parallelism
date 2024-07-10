from multiprocessing import Process as p
import sys, time

def func(i):
    
    print (f"calling func from process: {i}")
    time.sleep(5)
    for j in range (0,i):
        print(f"func output: {j}")

if __name__ == '__main__':
    scenario = int(sys.argv[1])
    n_process = int(sys.argv[2])

    for i in range(n_process):
        process = p(target= func, args=(i, ))
        process.start()
        #process.join()