import multiprocessing, sys

def function_square(data):
    return data * data

if __name__ == '__main__':
    scenario = int(sys.argv[1])
    n_inputs = int(sys.argv[2])

    inputs = list(range(0, n_inputs))
    pool = multiprocessing.Pool(processes=4)
    pool_outputs = pool.map(function_square, inputs)
    pool.close()
    pool.join()

    print ('Pool :', pool_outputs)
