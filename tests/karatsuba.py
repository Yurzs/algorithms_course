import random

from courses.karatsuba import multiply


def test_multiply():
    for x, y in [(random.randrange(0, 10000000000), random.randrange(0, 10000000000)) for _ in
                 range(1000)]:
        assert multiply(x, y) == x * y
