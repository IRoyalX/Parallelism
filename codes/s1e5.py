import time, sys, random, threading

class execution():
    def __init__(self):
        self.rlock = threading.RLock()
        self.total_items = 0

    def execute(self, value):
        with self.rlock:
            self.total_items += value

    def add(self):
        with self.rlock:
            self.execute(1)

    def remove(self):
        with self.rlock:
            self.execute(-1)

def adder(exec, items):
    print(f"{items} items to ADD\n")
    while items:
        exec.add()
        items -= 1
        if scenario != 2:
            time.sleep(0.2)
        print(f"+ One item ADDED, {items} remained.")

def remover(exec, items):
    print(f"\n{items} items to REMOVE\n")
    while items:
        exec.remove()
        items -= 1
        if scenario != 2:
            time.sleep(0.2)
        print(f"- One item REMOVED, {items} remained.")


if __name__ == "__main__":
    scenario = int(sys.argv[1])
   
    exec = execution()
    adder_thread = threading.Thread(target=adder, args=(exec, random.randint(10,15)))
    remover_thread = threading.Thread(target=remover, args=(exec, random.randint(5,10)))
    adder_thread.start()
    if scenario == 3:
        adder_thread.join()
    remover_thread.start()