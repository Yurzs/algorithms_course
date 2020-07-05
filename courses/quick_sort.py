import math
import random


class CallCounter:
    def __init__(self):
        self.counter = 0

    def __iadd__(self, other):
        self.counter += other

    def __call__(self, func):
        def wrap(array, left_index=None, right_index=None):
            if not left_index and not right_index:
                self.counter = 0
            if left_index is None:
                left_index = 0
            if right_index is None:
                right_index = len(array) - 1
            self.counter += abs(len(array[left_index:right_index]))
            return func(array, left_index, right_index)

        return wrap


counter = CallCounter()

CallCounter()


def quick_sort(array, left_index=None, right_index=None):
    if not left_index:
        left_index = 0
    if not right_index:
        right_index = len(array) - 1
    pivot_index = partition(array, left_index, right_index)
    if len(array[left_index:right_index]) == 1:
        return
    if pivot_index > left_index:
        quick_sort(array, left_index, pivot_index - 1)
    if pivot_index < right_index:
        quick_sort(array, pivot_index + 1, right_index)
    return array


def choose_pivot(start, stop):
    return random.randrange(start, stop)


def median_pivot(array, left_index, right_index):
    middle_index = math.floor((right_index - left_index) / 2) + left_index
    pivots = {
        array[left_index]: left_index,
        array[right_index]: right_index,
        array[middle_index]: middle_index,
    }
    sorted_pivots = sorted(pivots)
    return pivots[sorted_pivots[len(sorted_pivots) // 2]]


def partition(array, left_index, right_index):
    pivot_index = median_pivot(array, left_index, right_index)
    pivot = array[pivot_index]

    if pivot_index != left_index:
        array[left_index], array[pivot_index] = array[pivot_index], array[left_index]

    split_index = left_index + 1

    for array_index in range(split_index, right_index + 1):
        if pivot > array[array_index]:
            array[array_index], array[split_index] = array[split_index], array[array_index]
            split_index += 1

    array[split_index - 1], array[left_index] = array[left_index], array[split_index - 1]
    return split_index - 1
