import multiprocessing
import time, sys

def foo():
    print ('Starting function')
    for i in range(0,10):
        print(f"--> {i}\n")
        time.sleep(1)
    print ('Finished function')

if __name__ == '__main__':
    scenario = int(sys.argv[1])

    p = multiprocessing.Process(target=foo)
    print ('Process before execution:', p, p.is_alive())
    p.start()
    print ('Process running:', p, p.is_alive())
    p.terminate()
    print ('Process terminated:', p, p.is_alive())
    p.join()
    print ('Process joined:', p, p.is_alive())

    print ('Process exit code:', p.exitcode)