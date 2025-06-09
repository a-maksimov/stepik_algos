import math


def closest_exponent(n):
    if n <= 1:
        return 0
    return math.ceil(math.log2(n))

