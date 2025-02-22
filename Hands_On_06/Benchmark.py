import sys
import time
import random
import matplotlib.pyplot as plt

# Extend recursion limit for larger inputs
sys.setrecursionlimit(10**7)

# Fixed Pivot Quicksort
def split(arr, start, end):
    pivot_element = arr[start]  
    index = start + 1
    
    for pos in range(start + 1, end + 1):
        if arr[pos] < pivot_element:
            arr[index], arr[pos] = arr[pos], arr[index]
            index += 1
    
    arr[start], arr[index - 1] = arr[index - 1], arr[start]
    return index - 1

def quick_sort(arr, start, end):
    if start < end:
        pivot_location = split(arr, start, end)
        quick_sort(arr, start, pivot_location - 1)
        quick_sort(arr, pivot_location + 1, end)

def test_quick_sort_performance(arr):
    start_time = time.time()
    quick_sort(arr, 0, len(arr) - 1)
    end_time = time.time()
    return end_time - start_time

# Optimal scenario: Already Sorted Data
def best_case_scenario(size):
    return list(range(size))

# Worst scenario: Reverse Sorted Data
def worst_case_scenario(size):
    return list(range(size, 0, -1))

# Random scenario: Unordered Data
def average_case_scenario(size):
    return [random.randint(0, size) for _ in range(size)]

def evaluate_performance():
    dataset_sizes = [100, 200, 350, 500, 750, 1000, 2500, 5000, 7500, 10000]  
    best_case_results = []
    worst_case_results = []
    average_case_results = []

    # Running the benchmarks
    for size in dataset_sizes:
        # Best case scenario
        sorted_data = best_case_scenario(size)
        best_case_results.append(test_quick_sort_performance(sorted_data.copy()))

        # Worst case scenario
        reverse_sorted_data = worst_case_scenario(size)
        worst_case_results.append(test_quick_sort_performance(reverse_sorted_data.copy()))

        # Average case scenario
        random_data = average_case_scenario(size)
        average_case_results.append(test_quick_sort_performance(random_data.copy()))

    plt.plot(dataset_sizes, best_case_results, label="Best Case (Sorted List)", marker="o")
    plt.plot(dataset_sizes, worst_case_results, label="Worst Case (Reverse Sorted List)", marker="o")
    plt.plot(dataset_sizes, average_case_results, label="Average Case (Random List)", marker="o")

    plt.xlabel('Dataset Size (n)')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Quicksort Efficiency Analysis (Fixed Pivot)')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    evaluate_performance()
