def remove_duplicate_values(numbers_list: list):
    unique_index = 0
    unique_numbers = [numbers_list[unique_index]]
    
    for current_index in range(len(numbers_list)):
        if numbers_list[current_index] != unique_numbers[-1]:
            unique_numbers.append(numbers_list[current_index])
            unique_index += 1
    
    return unique_numbers

def start_program():
    # First test case
    sample_list = [2, 2, 2]
    result = remove_duplicate_values(sample_list)
    print(result)  # Output: [2]
    
    # Second test case
    sample_list = [1, 2, 2, 3, 4, 4, 4, 5, 5]
    result = remove_duplicate_values(sample_list)
    print(result)  # Output: [1, 2, 3, 4, 5]

if __name__ == '__main__':
    start_program()
