from sum_prime import find_prime_numbers_sum
import time
import concurrent.futures

def run_heavy_function(params):
    return find_prime_numbers_sum(*params)

def asychr():
    nb = [(1, 10000), (3, 50000), (5000, 100000), (4, 900), (800, 15000)]
    start_time = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=6) as executor:
        result = executor.map(run_heavy_function,nb)
    print(list(result))

    end_time = time.time()

    print(f'całkowity czas wykonaia zadania asynchronicznie: {end_time - start_time} s')
