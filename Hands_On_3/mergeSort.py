def merge_sort(numbers):
    if len(numbers) > 1:
        # Find the middle index
        middle = len(numbers) // 2
        left_part = numbers[:middle]
        right_part = numbers[middle:]

        # Recursively sort both halves
        merge_sort(left_part)
        merge_sort(right_part)

        left_index = right_index = merged_index = 0

        # Merge the sorted halves
        while left_index < len(left_part) and right_index < len(right_part):
            if left_part[left_index] < right_part[right_index]:
                numbers[merged_index] = left_part[left_index]
                left_index += 1
            else:
                numbers[merged_index] = right_part[right_index]
                right_index += 1
            merged_index += 1

        # Add remaining elements from left_part (if any)
        while left_index < len(left_part):
            numbers[merged_index] = left_part[left_index]
            left_index += 1
            merged_index += 1

        # Add remaining elements from right_part (if any)
        while right_index < len(right_part):
            numbers[merged_index] = right_part[right_index]
            right_index += 1
            merged_index += 1

# Test the merge sort function
unsorted_list = [5, 2, 4, 7, 1, 3, 2, 6]
print("Original list:", unsorted_list)
merge_sort(unsorted_list)
print("Sorted list:", unsorted_list)
