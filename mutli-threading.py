import numpy as np
import time  
from multiprocessing import Pool
import matplotlib.pyplot as plt
import psutil  

MATRIX_SIZE = 10
NUM_MATRICES = 5
constant_matrix = np.random.rand(MATRIX_SIZE, MATRIX_SIZE)

def multiply_matrix(matrix):
    return np.dot(matrix, constant_matrix)

def perform_multiplications(num_processes):
    random_matrices = [np.random.rand(MATRIX_SIZE, MATRIX_SIZE) for _ in range(NUM_MATRICES)]
    
    cpu_usage_before = psutil.cpu_percent(interval=None)
    
    start_time = time.time()  

    with Pool(processes=num_processes) as pool:
        pool.map(multiply_matrix, random_matrices)

    end_time = time.time() 
    cpu_usage_after = psutil.cpu_percent(interval=None)
    
    return end_time - start_time, cpu_usage_before, cpu_usage_after  
if __name__ == '__main__':
    thread_counts = range(1, 9)
    time_taken = []
    cpu_usage_before_list = []
    cpu_usage_after_list = []

    for threads in thread_counts:
        elapsed_time, cpu_before, cpu_after = perform_multiplications(threads)
        time_taken.append(elapsed_time)
        cpu_usage_before_list.append(cpu_before)
        cpu_usage_after_list.append(cpu_after)
        print(f"Threads: {threads} | Time taken: {elapsed_time:.2f} seconds | CPU Before: {cpu_before}% | CPU After: {cpu_after}%")

    plt.plot(thread_counts, time_taken, marker='o')
    plt.xlabel("Number of Threads")
    plt.ylabel("Time Taken (seconds)")
    plt.title("Execution Time")
    plt.grid()
    plt.show()

    for t, elapsed_time, cpu_before, cpu_after in zip(thread_counts, time_taken, cpu_usage_before_list, cpu_usage_after_list):
        print(f"Threads={t}: Time Taken={elapsed_time:.2f} seconds | CPU Before={cpu_before:.2f}% | CPU After={cpu_after:.2f}%")
