import random

# Non-Random Pivot QuickSort
def divide(arr, start, end):
    pivot_element = arr[start]
    pointer = start + 1  
    
    for index in range(start + 1, end + 1):
        if arr[index] < pivot_element:
            arr[pointer], arr[index] = arr[index], arr[pointer] 
            pointer += 1
    
    arr[start], arr[pointer - 1] = arr[pointer - 1], arr[start]
    return pointer - 1

def quick_sort_standard(arr, start, end):
    if start < end:
        split_index = divide(arr, start, end)
        quick_sort_standard(arr, start, split_index - 1) 
        quick_sort_standard(arr, split_index + 1, end) 

# Random Pivot QuickSort 
def divide_random(arr, start, end):
    random_pivot = random.randint(start, end) 
    arr[start], arr[random_pivot] = arr[random_pivot], arr[start]
    return divide(arr, start, end)

def quick_sort_randomized(arr, start, end):
    if start < end:
        split_index = divide_random(arr, start, end)
        quick_sort_randomized(arr, start, split_index - 1)  
        quick_sort_randomized(arr, split_index + 1, end) 

# Testing QuickSort Variations
def validate_sorting():
    test_cases = {
        "Scenario 1 - Pre-Sorted List": [1, 2, 3, 4, 5, 6],
        "Scenario 2 - Reverse Order": [6, 5, 4, 3, 2, 1],
        "Scenario 3 - Identical Elements": [5, 5, 5, 5, 5, 5],
        "Scenario 4 - Unordered List": [3, 1, 4, 2, 6, 5],
        "Scenario 5 - Mixed Positive & Negative": [-3, -6, 1, 2, -7, 5],
        "Scenario 6 - Wide Value Range": [1000, 200, 3000, 600, 150, 50],
        "Scenario 7 - No Elements": [],
        "Scenario 8 - Single Value": [1],
        "Scenario 9 - Small Sorted": [1, 2],
        "Scenario 10 - Small Unsorted": [2, 1]
    }

    for scenario, dataset in test_cases.items():
        # Handle empty case separately
        if len(dataset) == 0:
            print(f"{scenario}: [] (No Elements to Sort)")
            print("---------")
            continue
        
        # Applying Non-Random QuickSort
        dataset_copy = dataset.copy()  
        print(f"{scenario} (Fixed Pivot Sorting):")
        quick_sort_standard(dataset_copy, 0, len(dataset_copy) - 1)
        print("Output:", dataset_copy)
        
        # Applying Random Pivot QuickSort
        dataset_copy = dataset.copy()  
        print(f"{scenario} (Random Pivot Sorting):")
        quick_sort_randomized(dataset_copy, 0, len(dataset_copy) - 1)
        print("Output:", dataset_copy)
        print("---------")

if __name__ == "__main__":
    validate_sorting()
