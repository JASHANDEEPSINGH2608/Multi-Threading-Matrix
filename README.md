# Multiprocessing Matrix Multiplication

This project demonstrates how to perform matrix multiplication using multiple processes in Python. It measures the execution time and CPU usage before and after the computation, allowing for an analysis of how parallel processing affects performance.

## Overview

The script generates a constant matrix and multiple random matrices, then multiplies each random matrix by the constant matrix using the `multiprocessing` module. It captures the execution time and CPU usage, providing insights into how the number of threads impacts performance.

## Input

The script does not require any external input files. It generates:

- A constant matrix of size **50x50** filled with random values.
- **10 random matrices**, each of size **50x50**, that are multiplied by the constant matrix.

The number of threads (processes) used for the multiplication varies from **1 to 8**, as defined in the script.

## Usage

1. Clone the repository or download the script.
2. Run the script in a Python environment. You can execute the script from the command line:

```bash
python matrix_multiplication.py
```

3. The script will output the execution time and CPU usage for different thread counts (from 1 to 8) and generate a plot of execution time.

## How It Works

- The script creates a constant matrix of size **50x50** and generates **10 random matrices** of the same size.
- It measures the CPU usage before and after the multiplication using the `psutil` library.
- The `multiprocessing.Pool` is used to parallelize the multiplication process.
- The results, including time taken and CPU usage before and after the operation, are printed to the console and visualized in a plot.

## Output

The script prints the time taken and CPU usage for each thread count in the following format:

```
Threads: X | Time taken: Y seconds | CPU Before: A% | CPU After: B%
```

Where:
- `X` is the number of threads (1 to 8).
- `Y` is the time taken for the matrix multiplication in seconds.
- `A` is the CPU usage percentage before the operation.
- `B` is the CPU usage percentage after the operation.

### Example Output

```
Threads: 1 | Time taken: 0.15 seconds | CPU Before: 5.0% | CPU After: 25.0%
Threads: 2 | Time taken: 0.08 seconds | CPU Before: 5.0% | CPU After: 50.0%
Threads: 3 | Time taken: 0.07 seconds | CPU Before: 5.0% | CPU After: 75.0%
Threads: 4 | Time taken: 0.06 seconds | CPU Before: 5.0% | CPU After: 80.0%
Threads: 5 | Time taken: 0.05 seconds | CPU Before: 5.0% | CPU After: 85.0%
Threads: 6 | Time taken: 0.05 seconds | CPU Before: 5.0% | CPU After: 90.0%
Threads: 7 | Time taken: 0.04 seconds | CPU Before: 5.0% | CPU After: 90.0%
Threads: 8 | Time taken: 0.04 seconds | CPU Before: 5.0% | CPU After: 95.0%
```

### Visual Output

- A plot will be generated showing the execution time for different numbers of threads, with execution time on the y-axis and the number of threads on the x-axis.

## Conclusion

This project serves as a simple demonstration of how to use Python’s multiprocessing capabilities to speed up computations. It provides a basic framework that can be expanded for more complex matrix operations or other parallel processing tasks.
