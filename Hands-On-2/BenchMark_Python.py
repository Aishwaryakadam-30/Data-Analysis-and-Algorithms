# Python Code for Benchmarking Sorting Algorithms
# Name: Aishwarya Kadam | Student ID: 1002199035

import time
import random
import matplotlib.pyplot as plt

# Sorting algorithms
def selection_sort(dataset):
    for idx in range(len(dataset)):
        min_pos = idx
        for j in range(idx + 1, len(dataset)):
            if dataset[j] < dataset[min_pos]:
                min_pos = j
        dataset[idx], dataset[min_pos] = dataset[min_pos], dataset[idx]

def bubble_sort(dataset):
    for idx in range(len(dataset) - 1):
        is_swapped = False
        for j in range(len(dataset) - idx - 1):
            if dataset[j] > dataset[j + 1]:
                dataset[j], dataset[j + 1] = dataset[j + 1], dataset[j]
                is_swapped = True
        if not is_swapped:
            break

def insertion_sort(dataset):
    for idx in range(1, len(dataset)):
        current_value = dataset[idx]
        pos = idx - 1
        while pos >= 0 and dataset[pos] > current_value:
            dataset[pos + 1] = dataset[pos]
            pos -= 1
        dataset[pos + 1] = current_value

# Benchmarking function
def measure_sorting_time(sort_func, input_sizes):
    execution_times = []
    for size in input_sizes:
        random_data = [random.randint(-10000, 10000) for _ in range(size)]
        start_time = time.time()
        sort_func(random_data)
        end_time = time.time()
        execution_times.append(end_time - start_time)
    return execution_times

# Define input sizes for benchmarking
input_sizes = [5, 10, 20, 50, 100, 200, 500, 1000]

# Run benchmarks
selection_sort_times = measure_sorting_time(selection_sort, input_sizes)
bubble_sort_times = measure_sorting_time(bubble_sort, input_sizes)
insertion_sort_times = measure_sorting_time(insertion_sort, input_sizes)

# Plot results
plt.plot(input_sizes, selection_sort_times, label="Selection Sort", color='blue')
plt.plot(input_sizes, bubble_sort_times, label="Bubble Sort", color='orange')
plt.plot(input_sizes, insertion_sort_times, label="Insertion Sort", color='green')

plt.xlabel("Input Size (n)")
plt.ylabel("Time (seconds)")
plt.title("Benchmarking Sorting Algorithms")
plt.legend()
plt.grid(True)
plt.show()
