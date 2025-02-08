def merge_lists(first_list, second_list):
    first_index, second_index = 0, 0
    merged_list = []
    
    while first_index < len(first_list) and second_index < len(second_list):
        if first_list[first_index] < second_list[second_index]:
            merged_list.append(first_list[first_index])
            first_index += 1
        else:
            merged_list.append(second_list[second_index])
            second_index += 1
    
    while first_index < len(first_list):
        merged_list.append(first_list[first_index])
        first_index += 1
    while second_index < len(second_list):
        merged_list.append(second_list[second_index])
        second_index += 1
    
    return merged_list

def merge_multiple_lists(total_lists: int, list_length: int, *lists):
    all_lists = list(lists)
    
    while len(all_lists) > 1:
        temp_storage = []
        
        for i in range(0, len(all_lists), 2):
            if i + 1 < len(all_lists):
                temp_storage.append(merge_lists(all_lists[i], all_lists[i + 1]))
            else:
                temp_storage.append(all_lists[i])
        
        all_lists = temp_storage
    
    return all_lists[0]

def run_program():
    # Example 1
    number_of_lists = 3
    items_per_list = 4
    numbers1 = [1, 3, 5, 7]
    numbers2 = [2, 4, 6, 8]
    numbers3 = [0, 9, 10, 11]
    
    result = merge_multiple_lists(number_of_lists, items_per_list, numbers1, numbers2, numbers3)
    print(result)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    
    # Example 2
    number_of_lists = 3
    items_per_list = 3
    numbers1 = [1, 3, 7]
    numbers2 = [2, 4, 8]
    numbers3 = [9, 10, 11]
    
    result = merge_multiple_lists(number_of_lists, items_per_list, numbers1, numbers2, numbers3)
    print(result)  # Output: [1, 2, 3, 4, 7, 8, 9, 10, 11]

if __name__ == "__main__":
    run_program()
