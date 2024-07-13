from multiprocessing import Process as p, Semaphore, Queue
import sys, time

def func(i, scenario, s, output):
    output.put(f"calling func from process: {i}")
    if scenario != 1:
        time.sleep(0.2)
    with s:
        if scenario != 3:
            s.release()
        for j in range (0,i):
            output.put(f"func output: {j}")

if __name__ == "__main__":
    scenario = int(sys.argv[1])
    n_process = int(sys.argv[2])
    output = Queue()

    s = Semaphore(1)
    processes = []
    for i in range(n_process):
        process = p(target= func, args=(i, scenario, s, output))
        processes.append(process)
        process.start()
        if scenario != 2:
            process.join()
    
    for process in processes:
        process.join()
    while not output.empty():
        print(output.get())