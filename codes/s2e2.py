from multiprocessing import Process as p, Queue
import time, sys, multiprocessing as mp

def func(scenario, output):
    if scenario == 3:
        p(name= "insider", target= func, args=(None, output, )).start()
    name = mp.current_process().name
    output.put(f"Starting process name = {name}\n")
    time.sleep(1)
    output.put(f"Exiting process name = {name}\n")

if __name__ == "__main__":
    scenario = int(sys.argv[1])
    output = Queue()

    process_with_name = p(name="myFunc",target= func, args= (scenario, output, ))
    process_with_default_name = p(target= func, args=(None, output, ))
    
    process_with_name.start()
    if scenario == 2:
        process_with_name.join()
    process_with_default_name.start()

    process_with_name.join()
    process_with_default_name.join()
    while not output.empty():
        print(output.get())