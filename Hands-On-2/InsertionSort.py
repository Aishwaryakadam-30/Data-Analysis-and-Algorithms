# Insertion Sort Implementation
# ID: 1002199035
# Name: Aishwarya Kadam

# Function to perform insertion sort
def perform_insertion_sort(size, elements):
    for index in range(1, size):
        current_value = elements[index]
        position = index - 1
        # Move elements to find the correct position for current_value
        while position >= 0 and elements[position] > current_value:
            elements[position + 1] = elements[position]
            position -= 1
        elements[position + 1] = current_value

def run_insertion_sort_tests():
    # Test Case 1: Standard array
    test_case_1 = [8, 1, -4, 9, 3, -2, 5, 12]
    perform_insertion_sort(len(test_case_1), test_case_1)
    print("Test Case 1:", test_case_1)
    
    # Test Case 2: Empty array
    test_case_2 = []
    perform_insertion_sort(len(test_case_2), test_case_2)
    print("Test Case 2:", test_case_2)
    
    # Test Case 3: Single-element array
    test_case_3 = [3913]
    perform_insertion_sort(len(test_case_3), test_case_3)
    print("Test Case 3:", test_case_3)
    
    # Test Case 4: Already sorted array (Ascending order)
    test_case_4 = [11, 29, 35, 79, 96]
    perform_insertion_sort(len(test_case_4), test_case_4)
    print("Test Case 4:", test_case_4)
    
    # Test Case 5: Sorted array in descending order
    test_case_5 = [834, 765, 666, 432, 321, 2]
    perform_insertion_sort(len(test_case_5), test_case_5)
    print("Test Case 5:", test_case_5)
    
    # Test Case 6: Array with identical elements
    test_case_6 = [7777, 7777, 7777, 7777]
    perform_insertion_sort(len(test_case_6), test_case_6)
    print("Test Case 6:", test_case_6)
    
if __name__ == "__main__":
    run_insertion_sort_tests()

