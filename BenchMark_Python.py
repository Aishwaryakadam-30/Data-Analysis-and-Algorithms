# Python Code for Benchmarking Sorting Algorithms
# Name: Aishwarya Kadam
# Student ID: 1002199035

import time
import random
import matplotlib.pyplot as plt

# Selection Sort Algorithm
def selection_sort(data):
    length = len(data)
    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if data[j] < data[min_index]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]

# Bubble Sort Algorithm
def bubble_sort(data):
    length = len(data)
    for i in range(length - 1):
        swapped = False
        for j in range(length - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
        if not swapped:
            break

# Insertion Sort Algorithm
def insertion_sort(data):
    length = len(data)
    for i in range(1, length):
        current_value = data[i]
        position = i - 1
        while position >= 0 and data[position] > current_value:
            data[position + 1] = data[position]
            position -= 1
        data[position + 1] = current_value

# Measure execution time of sorting algorithms
def evaluate_sorting_performance(sort_function, test_sizes):
    execution_times = []
    for size in test_sizes:
        # Create a random array of integers
        array = [random.randint(-10000, 10000) for _ in range(size)]
        
        start = time.time()
        sort_function(array)
        end = time.time()
        
        execution_times.append(end - start)
    
    return execution_times

# Visualizing performance results
def display_performance_graph(test_sizes, sel_times, bub_times, ins_times):
    plt.figure(figsize=(10, 6))
    
    plt.plot(test_sizes, sel_times, label="Selection Sort")
    plt.plot(test_sizes, bub_times, label="Bubble Sort")
    plt.plot(test_sizes, ins_times, label="Insertion Sort")
    
    plt.xlabel("Input Size (n)")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Sorting Algorithms Performance Analysis")
    plt.legend()
    plt.grid(True)
    plt.show()

# Define test sizes for the benchmarking
test_sizes = [5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 25000, 50000, 75000]

# Running the performance evaluation
selection_results = evaluate_sorting_performance(selection_sort, test_sizes)
bubble_results = evaluate_sorting_performance(bubble_sort, test_sizes)
insertion_results = evaluate_sorting_performance(insertion_sort, test_sizes)

# Generate performance comparison graph
display_performance_graph(test_sizes, selection_results, bubble_results, insertion_results)
