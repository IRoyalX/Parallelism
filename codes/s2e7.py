import multiprocessing, sys
from multiprocessing import Barrier, Lock, Process, Queue
from time import time
from datetime import datetime

def test_with_barrier(synchronizer, serializer, scenario, output):
    name = multiprocessing.current_process().name
    if scenario != 2:
        synchronizer.wait()
    now = time()
    with serializer:
        output.put(f"process {name}:\n{datetime.fromtimestamp(now)}\n")

def test_without_barrier(output):
    name = multiprocessing.current_process().name
    now = time()
    output.put(f"process {name}:\n{datetime.fromtimestamp(now)}\n")


if __name__ == "__main__":
    scenario = int(sys.argv[1])
    output = Queue()

    synchronizer = Barrier(2)
    serializer = Lock()
    p1= Process(name="p1 - test_with_barrier", target=test_with_barrier, args=(synchronizer,serializer, scenario, output))
    p1.start()
    p2= Process(name="p2 - test_with_barrier", target=test_with_barrier, args=(synchronizer,serializer, scenario, output))
    p2.start()
    if scenario == 3:
        p1.join()
        p2.join()
    p3= Process(name="p3 - test_without_barrier", target=test_without_barrier, args= (output, ))
    p3.start()
    p4= Process(name="p4 - test_without_barrier", target=test_without_barrier, args= (output, ))
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
    while not output.empty():
        print(output.get())
