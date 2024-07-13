import multiprocessing, sys, time

class MyClass(multiprocessing.Process):
    def run(self):
        time.sleep(0.5)
        print (f"called run method by {self.name}")

if __name__ == "__main__":
    scenario = int(sys.argv[1])
    n_process = int(sys.argv[2])

    for i in range(n_process):
        process = MyClass()
        process.start()
        if scenario == 1:
            process.join()
        elif scenario == 3 and i%2 == 0:
            process.join()
            