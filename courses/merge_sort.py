import math


def get_item_or_inf(array, index):
    try:
        return array[index]
    except IndexError:
        return - math.inf


def merge_sort(input_array: list):
    left_array = input_array[0: int(len(input_array) / 2)]
    right_array = input_array[int(len(input_array) / 2):]
    if len(left_array) > 2:
        left_array = merge_sort(left_array)
    elif len(right_array) > 2:
        right_array = merge_sort(right_array)
    left_array_pos = 0
    right_array_pos = 0
    result_array = []
    for _ in range(len(input_array)):
        if left_array[left_array_pos:left_array_pos] < right_array[right_array_pos]:
            result_array.append(left_array[left_array_pos])
            left_array_pos += 1
        elif right_array[right_array_pos] < left_array[left_array_pos]:
            result_array.append(right_array[right_array_pos])
            right_array_pos += 1
    return result_array
