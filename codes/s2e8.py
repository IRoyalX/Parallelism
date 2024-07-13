import multiprocessing, sys, time, random

def function_square(data):
    time.sleep(random.randrange(0,2))
    return data * data

def function_square_print(data):
    time.sleep(random.randrange(0,2))
    print("-->",data * data)

if __name__ == "__main__":
    scenario = int(sys.argv[1])
    n_inputs = int(sys.argv[2])

    inputs = list(range(0, n_inputs))
    pool = multiprocessing.Pool(processes=2)
    
    if scenario == 2:
        pool.map(function_square_print, inputs)
    if scenario  != 2:
        pool_outputs = pool.map(function_square, inputs)
        for output in pool_outputs:
            print(f"--> {output}")

    pool.close()
    if scenario != 3:
        pool.join()

