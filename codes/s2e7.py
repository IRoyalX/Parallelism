import multiprocessing, sys
from multiprocessing import Barrier, Lock, Process
from time import time
from datetime import datetime

def test_with_barrier(synchronizer, serializer, scenario):
    name = multiprocessing.current_process().name
    if scenario != 2:
        synchronizer.wait()
    now = time()
    with serializer:
        print(f"process {name}:\n{datetime.fromtimestamp(now)}\n")

def test_without_barrier():
    name = multiprocessing.current_process().name
    now = time()
    print(f"process {name}:\n{datetime.fromtimestamp(now)}\n")


if __name__ == "__main__":
    scenario = int(sys.argv[1])

    synchronizer = Barrier(2)
    serializer = Lock()
    p1= Process(name="p1 - test_with_barrier", target=test_with_barrier, args=(synchronizer,serializer, scenario))
    p1.start()
    p2= Process(name="p2 - test_with_barrier", target=test_with_barrier, args=(synchronizer,serializer, scenario))
    p2.start()
    if scenario == 3:
        p1.join()
        p2.join()
    Process(name="p3 - test_without_barrier", target=test_without_barrier).start()
    Process(name="p4 - test_without_barrier", target=test_without_barrier).start()
