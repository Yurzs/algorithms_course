def sort_and_count(array):
    array_len = len(array)
    if array_len == 1:
        return array, 0
    else:
        half = array_len // 2
        sorted_array_left, inv_left = sort_and_count(array[:half])
        sorted_array_right, inv_right = sort_and_count(array[half:])
        sorted_array, inversions = merge_and_count_split_inversions(sorted_array_left,
                                                                    sorted_array_right,
                                                                    array_len)
        return sorted_array, inv_left + inv_right + inversions


def merge_and_count_split_inversions(left_array: list, right_array: list, array_len: int):
    sorted_array = []
    inversion_counter = 0
    left_index = 0
    right_index = 0
    for main_index in range(array_len):
        if left_index < len(left_array):
            left_item = left_array[left_index]
        else:
            return sorted_array + right_array[right_index:], inversion_counter
        if right_index < len(right_array):
            right_item = right_array[right_index]
        else:
            return sorted_array + left_array[left_index:], inversion_counter
        if left_item < right_item:
            sorted_array.append(left_item)
            left_index += 1
        elif right_item < left_item:
            sorted_array.append(right_item)
            inversion_counter += len(left_array[left_index:])
            right_index += 1
    return sorted_array, inversion_counter
