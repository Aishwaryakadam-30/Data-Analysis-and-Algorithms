# Bubble Sort Implementation
# Name: Aishwarya Kadam
# Student ID: 1002199035


# Bubble sort function
def sort_using_bubble(length, array):
    for i in range(length - 1):
        has_swapped = False
        for j in range(length - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                has_swapped = True
        # Terminate early if the array is already sorted
        if not has_swapped:
            return

def run_tests():
    # Test Case 1: General unsorted array
    test1 = [8, 1, -4, 9, 3, -2, 5, 12]
    sort_using_bubble(len(test1), test1)
    print("Test Case 1:", test1)

    # Test Case 2: Empty array
    test2 = []
    sort_using_bubble(len(test2), test2)
    print("Test Case 2:", test2)

    # Test Case 3: Single element array
    test3 = [3913]
    sort_using_bubble(len(test3), test3)
    print("Test Case 3:", test3)

    # Test Case 4: Already sorted array in ascending order
    test4 = [11, 29, 35, 79, 96]
    sort_using_bubble(len(test4), test4)
    print("Test Case 4:", test4)

    # Test Case 5: Sorted array in descending order
    test5 = [834, 765, 666, 432, 321, 2]
    sort_using_bubble(len(test5), test5)
    print("Test Case 5:", test5)

    # Test Case 6: Array with duplicate elements
    test6 = [7777, 7777, 7777, 7777]
    sort_using_bubble(len(test6), test6)
    print("Test Case 6:", test6)

if __name__ == "__main__":
    run_tests()
