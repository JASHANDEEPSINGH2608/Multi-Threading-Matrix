# Multiprocessing Matrix Multiplication

This project demonstrates how to perform matrix multiplication using multiple processes in Python. It measures the execution time and CPU usage before and after the computation, allowing for an analysis of how parallel processing affects performance.

## Overview

The script generates a constant matrix and multiple random matrices, then multiplies each random matrix by the constant matrix using the `multiprocessing` module. It captures the execution time and CPU usage, providing insights into how the number of threads impacts performance.

## Input

The script does not require any external input files. It generates:

- A constant matrix of size **10x10** filled with random values.
- **5 random matrices**, each of size **10x10**, that are multiplied by the constant matrix.

The number of threads (processes) used for the multiplication varies from **1 to 8**, as defined in the script.

## How It Works

- The script creates a constant matrix of size **10x10** and generates **5 random matrices** of the same size.
- It measures the CPU usage before and after the multiplication using the `psutil` library.
- The `multiprocessing.Pool` is used to parallelize the multiplication process.
- The results, including time taken and CPU usage before and after the operation, are printed to the console and visualized in a plot.

### Example Output

```
Threads: 1 | Time taken: 0.15 seconds | CPU Before: 5.0% | CPU After: 25.0%
Threads: 2 | Time taken: 0.08 seconds | CPU Before: 5.0% | CPU After: 50.0%
Threads: 3 | Time taken: 0.07 seconds | CPU Before: 5.0% | CPU After: 76.0%
Threads: 4 | Time taken: 0.06 seconds | CPU Before: 5.0% | CPU After: 80.0%
Threads: 5 | Time taken: 0.05 seconds | CPU Before: 5.0% | CPU After: 83.0%
Threads: 6 | Time taken: 0.05 seconds | CPU Before: 5.0% | CPU After: 90.0%
Threads: 7 | Time taken: 0.04 seconds | CPU Before: 5.0% | CPU After: 90.0%
Threads: 8 | Time taken: 0.04 seconds | CPU Before: 5.0% | CPU After: 94.0%
```


