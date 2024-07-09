import multiprocessing, sys

class MyProcess(multiprocessing.Process):
    def run(self):
        print (f"called run method by {self.name}")
        return

if __name__ == '__main__':
    scenario = int(sys.argv[1])
    n_process = int(sys.argv[2])

    for i in range(n_process):
        process = MyProcess()
        process.start()
        process.join()