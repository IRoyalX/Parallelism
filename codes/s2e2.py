from multiprocessing import Process as p
import time, sys, multiprocessing as mp

def func(scenario):
    if scenario == 3:
        p(name= "insider", target= func, args=(None, )).start()
    name = mp.current_process().name
    print (f"Starting process name = {name}\n")
    time.sleep(1)
    print (f"Exiting process name = {name}\n")

if __name__ == "__main__":
    scenario = int(sys.argv[1])

    process_with_name = p(name="myFunc process",target= func, args= (scenario, ))
    process_with_default_name = p(target= func, args=(None, ))
    
    process_with_name.start()
    if scenario == 2:
        process_with_name.join()
    process_with_default_name.start()
    process_with_name.join()
    process_with_default_name.join()