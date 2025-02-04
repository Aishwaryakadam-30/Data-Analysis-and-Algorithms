import time
import numpy as np
import matplotlib.pyplot as plt

# Function to analyze
def count_operations(size):
    total_count = 1
    for _ in range(size):
        for _ in range(size):
            total_count += 1
    return total_count

# Range of input sizes
input_sizes = list(range(1, 1000))
execution_times = []

# Measure execution time
for current_size in input_sizes:
    start_time = time.time()
    count_operations(current_size)
    end_time = time.time()
    execution_times.append(end_time - start_time)

# Convert lists to numpy arrays for curve fitting
size_array = np.array(input_sizes)
time_array = np.array(execution_times)

# Perform quadratic curve fitting
quadratic_coefficients = np.polyfit(size_array, time_array, 2)
fitted_execution_times = np.polyval(quadratic_coefficients, input_sizes)

# Plot actual execution time vs fitted quadratic curve
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, execution_times, label="Measured Time")
plt.plot(input_sizes, fitted_execution_times, label="Quadratic Fit", color='r')
plt.xlabel('Input Size')
plt.ylabel('Execution Time (Seconds)')
plt.title('Execution Time vs Input Size')
plt.legend()
plt.grid(True)
plt.show()

# Determine asymptotic bounds (Big-O, Big-Omega, Big-Theta)
upper_bound = quadratic_coefficients[0] * size_array**2
lower_bound = quadratic_coefficients[0] * size_array**2 * 0.8  # Example scaling factor for lower bound

# Plot bounds
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, execution_times, label="Measured Time")
plt.plot(input_sizes, fitted_execution_times, label="Quadratic Fit", color='r')
plt.plot(input_sizes, upper_bound, label="Upper Bound", color='g')
plt.plot(input_sizes, lower_bound, label="Lower Bound", color='orange')
plt.xlabel('Input Size')
plt.ylabel('Execution Time (Seconds)')
plt.title('Upper and Lower Bounds of Execution Time')
plt.legend()
plt.grid(True)
plt.show()

# Approximate n_0 where actual time surpasses the fitted curve
threshold_index = np.where(time_array > fitted_execution_times)[0][0]

plt.figure(figsize=(10, 6))
plt.plot(input_sizes, execution_times, label="Measured Time")
plt.plot(input_sizes, fitted_execution_times, label="Quadratic Fit", color='r')
plt.axvline(x=input_sizes[threshold_index], color='k', linestyle='--', label=f"n_0 ~ {input_sizes[threshold_index]}")
plt.xlabel('Input Size')
plt.ylabel('Execution Time (Seconds)')
plt.title('Estimating n_0 (Threshold Point)')
plt.legend()
plt.grid(True)
plt.show()

print(f"Estimated n_0: {input_sizes[threshold_index]}")
