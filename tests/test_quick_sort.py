import random

from courses.quick_sort import quick_sort, counter


def test_quick_sort():
    array = [x for x in range(7)]
    random.shuffle(array)
    print(array)
    assert quick_sort(array) == sorted(array)
    print(counter.counter)
