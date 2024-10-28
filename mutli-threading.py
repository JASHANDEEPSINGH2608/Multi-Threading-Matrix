import numpy as np
import time
from multiprocessing import Pool
import matplotlib.pyplot as plt
import psutil
import tracemalloc
import threading

# Define the matrix multiplication function outside of main
def multiply_matrices(matrix_constant_tuple):
    matrix, constant_matrix = matrix_constant_tuple
    return np.dot(matrix, constant_matrix)

def execute_multiprocessing(num_threads, matrices, constant_matrix, cpu_usage_log):
    start_time = time.time()
    print(f"Running with {num_threads} processes...")

    # Prepare the data as tuples of (matrix, constant_matrix) for each multiplication
    data = [(matrix, constant_matrix) for matrix in matrices]
    
    # Start CPU monitoring in a separate thread
    cpu_monitoring_thread = threading.Thread(target=monitor_cpu_usage, args=(cpu_usage_log,))
    cpu_monitoring_thread.start()
    
    with Pool(processes=num_threads) as pool:
        results = pool.map(multiply_matrices, data, chunksize=1)

    # Stop CPU monitoring after computation
    global monitoring
    monitoring = False
    cpu_monitoring_thread.join()

    end_time = time.time()
    print(f"Execution completed with {num_threads} processes.")
    return (end_time - start_time) / 60  # Return time in minutes

# Function to monitor CPU usage
monitoring = True
def monitor_cpu_usage(cpu_usage_log, interval=0.5):
    """Records CPU usage every `interval` seconds."""
    while monitoring:
        cpu_usage_log.append(psutil.cpu_percent(interval=interval, percpu=True))

def plot_cpu_usage(cpu_usage_log):
    """Plots CPU usage per core over time."""
    # Transpose the list of lists to get usage per core over time
    cpu_usage_log = list(zip(*cpu_usage_log))
    time_points = list(range(len(cpu_usage_log[0])))  # X-axis (time points)

    plt.figure(figsize=(10, 6))
    for i, core_usage in enumerate(cpu_usage_log):
        plt.plot(time_points, core_usage, label=f'CPU {i}')
    
    plt.xlabel("Time (in intervals)")
    plt.ylabel("CPU Usage (%)")
    plt.title("CPU Usage per Core Over Time")
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    # Adjusted parameters to test in a manageable way
    num_matrices = 5    # Start with 5 matrices for testing
    matrix_size = 10    # Smaller matrix size for testing

    # Generate smaller matrices
    print("Generating matrices...")
    matrices = [np.random.rand(matrix_size, matrix_size) for _ in range(num_matrices)]
    constant_matrix = np.random.rand(matrix_size, matrix_size)
    print("Matrices generated.")

    # Log CPU usage
    cpu_usage_log = []

    # Run for a single thread to test
    try:
        tracemalloc.start()  # Start memory monitoring
        exec_time = execute_multiprocessing(1, matrices, constant_matrix, cpu_usage_log)  # Start with 1 thread only for testing
        print(f"Time Taken={exec_time:.2f} mins")

        # Plot the execution time (for demonstration)
        plt.plot([1], [exec_time], marker='o', color='b')
        plt.xlabel('Number of Processes')
        plt.ylabel('Time Taken (mins)')
        plt.title('Execution Time with Limited Process')
        plt.grid(True)
        plt.show()

        # Plot the CPU usage
        plot_cpu_usage(cpu_usage_log)

        # Display memory usage
        current, peak = tracemalloc.get_traced_memory()
        print(f"Current memory usage: {current / 10**6} MB; Peak: {peak / 10**6} MB")
        tracemalloc.stop()

    except Exception as e:
        print("Execution stopped due to an error:", e)

# Ensuring code runs in the main block
if __name__ == '__main__':
    main()
