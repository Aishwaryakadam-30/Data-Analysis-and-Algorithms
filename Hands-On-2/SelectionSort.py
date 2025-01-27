# Selection Sort Implementation
# ID: 1002199035
# Name: Aishwarya Kadam

# Function to perform selection sort
def selection_sort(size, elements):
    for index in range(size):
        min_index = index
        # Find the minimum value in the remaining unsorted part
        for j in range(index + 1, size):
            if elements[j] < elements[min_index]:
                min_index = j
        # Swap the minimum element with the current element
        elements[index], elements[min_index] = elements[min_index], elements[index]

def run_selection_sort_tests():
    # Test Case 1: General unsorted array
    test_case_1 = [8, 1, -4, 9, 3, -2, 5, 12]
    selection_sort(len(test_case_1), test_case_1)
    print("Test Case 1:", test_case_1)
    
    # Test Case 2: Empty array
    test_case_2 = []
    selection_sort(len(test_case_2), test_case_2)
    print("Test Case 2:", test_case_2)
    
    # Test Case 3: Single-element array
    test_case_3 = [3913]
    selection_sort(len(test_case_3), test_case_3)
    print("Test Case 3:", test_case_3)
    
    # Test Case 4: Already sorted array (Ascending order)
    test_case_4 = [11, 29, 35, 79, 96]
    selection_sort(len(test_case_4), test_case_4)
    print("Test Case 4:", test_case_4)
    
    # Test Case 5: Sorted array in descending order
    test_case_5 = [834, 765, 666, 432, 321, 2]
    selection_sort(len(test_case_5), test_case_5)
    print("Test Case 5:", test_case_5)
    
    # Test Case 6: Array with identical elements
    test_case_6 = [7777, 7777, 7777, 7777]
    selection_sort(len(test_case_6), test_case_6)
    print("Test Case 6:", test_case_6)

if __name__ == "__main__":
    run_selection_sort_tests()
